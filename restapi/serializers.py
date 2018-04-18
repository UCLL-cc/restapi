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


class DayListSerializer(serializers.ModelSerializer):
    triggers = TriggerSerializer(many=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Day
        fields = ('id', 'date', 'triggers')
