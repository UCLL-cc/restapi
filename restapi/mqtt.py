import logging
import asyncio
import os

from hbmqtt.broker import Broker


class AsyncMqttBroker:

    @asyncio.coroutine
    def broker(self):
        config = {
            'listeners': {
                'default': {
                    'type': 'tcp',
                    'bind': '0.0.0.0:1883',
                },
                'ws-mqtt': {
                    'bind': '127.0.0.1:8080',
                    'type': 'ws',
                    'max_connections': 10,
                },
            },
            'sys_interval': 10,
            'auth': {
                'allow-anonymous': True,
                'password-file': os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwd"),
                'plugins': [
                    'auth_file', 'auth_anonymous'
                ]

            }
        }

        broker = Broker(config)
        yield from broker.start()

    def __init__(self):
        formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
        logging.basicConfig(level=logging.INFO, format=formatter)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.broker())
        asyncio.get_event_loop().run_forever()
