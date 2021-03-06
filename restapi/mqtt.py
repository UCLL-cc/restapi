from datetime import datetime, timedelta, time

import pytz
from django.utils import timezone
import paho.mqtt.client as mqtt


class AsyncMQTTClient:
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        try:
            from restapi.models import Trigger, Day
            if not msg.topic == 'trigger':
                return

            today = datetime.now().date()
            tomorrow = today + timedelta(1)

            today_start = datetime.combine(today, time())
            today_end = datetime.combine(tomorrow, time())

            day = Day.objects.order_by('-date').filter(date__gte=today_start).filter(date__lt=today_end).first()

            if not day:
                day = Day(date=datetime.now().date())
                day.save()
            else:
                pass

            time1 = pytz.timezone('Europe/Brussels');
            trigger = Trigger(time=datetime.now(time1).time(), day=day)
            trigger.save()
        except Exception:
            pass

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set('bjprbmwc', password='BjEbmRkVwazu')
    client.connect("m23.cloudmqtt.com", 17184, 60)

    client.subscribe('trigger', qos=1)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_start()
