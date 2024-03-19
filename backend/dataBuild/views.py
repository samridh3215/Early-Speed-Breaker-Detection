from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from dataBuild.models import SpeedBreakerData
from django.db.models import F
import json
from keras.models import load_model
import pandas as pd 
from scipy.signal import butter, filtfilt

# def butter_lowpass(cutoff, fs, order=5):
#     nyquist = 0.5 * fs
#     normal_cutoff = cutoff / nyquist
#     b, a = butter(order, normal_cutoff, btype='low', analog=False)
#     return b, a

# def apply_lowpass_filter(data, cutoff_frequency, sampling_frequency):
#     b, a = butter_lowpass(cutoff_frequency, sampling_frequency)
#     filtered_data = filtfilt(b, a, data)
#     return filtered_data

# cutoff_frequency = 10  # Adjust cutoff frequency as needed
# sampling_frequency = 100  # Assuming sampling frequency of 100 Hz, adjust accordingly

# # Apply low-pass filter to specified columns
# columns_to_filter = ['Linear Acceleration x (m/s^2)',
#                      'Linear Acceleration y (m/s^2)',
#                      'Linear Acceleration z (m/s^2)',
#                      'Absolute acceleration (m/s^2)']



# model = load_model('/home/samridh/Projects/Kalpaana/backend/trained_model.h5')

# Create your views here.
def hello(request):
    if request.method=="GET" :
        data = list(SpeedBreakerData.objects.all())
        return render(request, 'home.html', {"data":data})
@csrf_exempt
def addData(request, buffer, lat, long):
    if request.method == "POST" :
        # print(request.header)
   
        try:
            if SpeedBreakerData.objects.filter(lat = lat,long = long).exists():
                SpeedBreakerData.objects.filter(lat = lat,long = long).update(tally = F("tally")+1)
                return HttpResponse({"Message":"Added tally"},  status=200)
            else:
                data = SpeedBreakerData.objects.create(
                    lat = lat,
                    long = long,
                    tally = 0).save()
                return HttpResponse({"Message":"added"}, status=200)
        except Exception as e:
            print(e)
            return HttpResponse({"Message":f"Error - {e}"}, status=400)
@csrf_exempt    
def recieveData(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        print(data)
        ##run ml model
        # df = pd.DataFrame(data['buffer'])
        # for c in range(4):
        #     df[c] = apply_lowpass_filter(df[c], cutoff_frequency, sampling_frequency)
        # print(df)
        # model.predict(df)
        
        return addData(request, data['buffer'], data['lat'], data['long'])
        # return HttpResponse({"Message":"Recieved gracefully"}, status=200)