from datetime import date, time
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from sendAlert.models import Devices
from django.views.decorators.csrf import csrf_exempt
import threading
import time as t
Time = time()
# Create your views here.
def createConnectionPool(request):
    if request.method=="GET":
        if Devices.objects.filter(ip=request.META['REMOTE_ADDR']).exists():
            return render(request, 'connection.html', {"exist":1})
            return HttpResponse("Already Connected...\n", status=200)
        else:
            Devices.objects.create(
                ip = request.META['REMOTE_ADDR'],
                connectionDate = date.today(),
                connectionTime= Time.isoformat(),
            ).save()
            return render(request, 'connection.html', {"exist":0})
            return HttpResponse("Connected", status=200)
def send():
    while True:
        for d in Devices.objects.all():
            print(d.ip, end=', ')
        t.sleep(2.0)

# alertThread = threading.Thread(name='alert', target=send, daemon=True)
# alertThread.run()

@csrf_exempt
def endConnection(request):
    if(request.method=="POST"):
        if Devices.objects.filter(ip=request.META['REMOTE_ADDR']).exists():
            Devices.objects.filter(ip=request.META['REMOTE_ADDR']).delete()
        return HttpResponse("Connection Ended", status=200)