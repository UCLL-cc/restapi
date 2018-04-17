from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from restapi.serializers import TriggerSerializer, DaySerializer
from restapi.models import Trigger, Day


@csrf_exempt
def trigger_list(request):
    if request.method == 'GET':
        triggers = Trigger.objects.all()
        serializer = TriggerSerializer(triggers, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def day_list(request):
    if request.method == 'GET':
        days = Day.objects.all()
        serializer = DaySerializer(days, many=True)
        return JsonResponse(serializer.data, safe=False)
