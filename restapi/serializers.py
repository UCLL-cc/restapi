import math
from datetime import datetime, timedelta, date, time

import pytz
from rest_framework import serializers
from restapi.models import Trigger, Day


class TriggerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Trigger
        fields = ('id', 'time')


class DaySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Day
        fields = ('id', 'date')


class CustomClass(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TriggerGroupSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    time = serializers.TimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


def round_minutes(dt, minutes):
    new_minute = (dt.minute // minutes + 1) * minutes
    return dt + timedelta(minutes=new_minute - dt.minute)


class FinalSerializer(serializers.Serializer):
    triggers = TriggerGroupSerializer(many=True)
    predicted = TriggerGroupSerializer()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class DayListSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def get_data(self, obj):
        data = list(obj.triggers.all())
        final = list()

        begin = datetime.strptime('00:00', '%H:%M')
        stop = datetime.strptime('23:30', '%H:%M').time()
        delta = timedelta(minutes=30)

        while True:
            end = datetime.combine(date(1, 1, 1), begin.time()) + delta
            result = list()
            for x in data:
                if begin.time() <= x.time <= end.time():
                    result.append(x)

            final.append(CustomClass(count=len(result), time=begin.time().strftime('%H:%M')))

            if begin.time() == stop:
                break
            begin = end

        time1 = pytz.timezone('Europe/Brussels')
        time_now_rounded = round_minutes(datetime.now(time1), 30)
        amount_last_average = 3
        sum = 0

        if obj.date == datetime.today().date():
            for x in final:
                for i in range(1, amount_last_average):
                    z = time_now_rounded - (delta * i)
                    if x.time == z.time().strftime('%H:%M'):
                        sum += x.count

        real_final = CustomClass(
            predicted=CustomClass(count=sum / amount_last_average, time=time_now_rounded.time().strftime('%H:%M')),
            triggers=final)

        return FinalSerializer(real_final).data

    class Meta:
        model = Day
        fields = ('id', 'date', 'data')
