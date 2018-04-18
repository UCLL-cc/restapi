from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.response import Response

from restapi.serializers import TriggerSerializer, DaySerializer, DayListSerializer
from restapi.models import Trigger, Day
from rest_framework import viewsets


class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer


class DayViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Day.objects.all()
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Day.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DayListSerializer(user)
        return Response(serializer.data)

