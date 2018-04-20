from datetime import datetime, timedelta, date, time
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


class TriggerGroup(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TriggerGroupSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    time = serializers.TimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class DayListSerializer(serializers.ModelSerializer):
    triggers = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def get_count(self, obj):
        return obj.triggers.count()

    def get_triggers(self, obj):
        data = list(obj.triggers.all())
        begin = datetime.strptime('00:00', '%H:%M')
        delta = timedelta(minutes=30)
        final = list()
        stop = datetime.strptime('23:30', '%H:%M').time()

        while True:
            end = datetime.combine(date(1, 1, 1), begin.time()) + delta
            result = list()
            for x in data:
                if begin.time() <= x.time <= end.time():
                    result.append(x)
                    data.remove(x)

            final.append(TriggerGroup(count=len(result), time=begin.time().strftime('%H:%M')))

            if begin.time() == stop:
                break
            begin = end

        return TriggerGroupSerializer(final, many=True).data

    class Meta:
        model = Day
        fields = ('id', 'date', 'triggers', 'count')
