from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response

from restapi.serializers import TriggerSerializer, DaySerializer
from restapi.models import Trigger, Day
from rest_framework import viewsets
from rest_framework.mixins import (RetrieveModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin)


class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer


class DayViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    lookup_field = 'id'
