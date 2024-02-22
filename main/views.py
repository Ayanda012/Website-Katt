import os
from django.shortcuts import render
import joblib
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
import pickle
import json
import joblib
from django.http import JsonResponse
from sklearn.ensemble import RandomForestClassifier




# Create your views here.
def main (request):

    return render(request, 'index.html')

def equipment(request):

    return render(request, 'extra/equipment.html')

def recommendations(request):

    return render(request, 'tailored_recommendations.html')

def prediction(request):

    if request.method == "GET":
        latitude = request.GET.get('latitude_input')
        longitude = request.GET.get('longitude_input')

        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": {latitude},
            "longitude": {longitude},
            "current": "relative_humidity_2m",
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "wind_speed_10m_max", "shortwave_radiation_sum"],
            "timezone": "auto"
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
        current = response.Current()
        current_relative_humidity_2m = current.Variables(0).Value()
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
        daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
        daily_wind_speed_10m_max = daily.Variables(3).ValuesAsNumpy()
        daily_shortwave_radiation_sum = daily.Variables(4).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s"),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["precipitation_sum"] = daily_precipitation_sum
        daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
        daily_data["shortwave_radiation_sum"] = daily_shortwave_radiation_sum

        daily_dataframe = pd.DataFrame(data = daily_data)
        daily_dataframe = daily_dataframe.rename(columns = {'temperature_2m_max':'Max Temperature',
                                          'temperature_2m_min' : 'Min Temperature',
                                          'precipitation_sum' : 'Precipitation',
                                          'wind_speed_10m_max' : 'Wind',
                                          'shortwave_radiation_sum' : 'Solar'})
        
        daily_dataframe['Relative Humidity'] = current_relative_humidity_2m
        daily_dataframe['Solar'] = daily_dataframe['Solar']*10
        model_path = os.path.join(os.path.dirname(__file__), 'model', 'PSE_model.pkl')
        pse_model = joblib.load(model_path)
        solar_energy_prediction = pse_model.predict(daily_dataframe[['Max Temperature', 'Min Temperature', 'Precipitation', 'Wind', 'Relative Humidity', 'Solar']])
        daily_dataframe['Potential Solar Energy'] = solar_energy_prediction/1000
        daily_dataframe['formatted_date'] = daily_dataframe['date'].dt.strftime('%d %B')
        context = {
            'daily_dataframe': daily_dataframe,
            'potential_solar_energy_data': daily_dataframe['Potential Solar Energy'].tolist(),
            'categories': daily_dataframe['formatted_date'].tolist(),
        }
    return render(request, 'extra/prediction_results.html', context)



# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def main (request):
   
    return render(request,'index.html')

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or send an email
            pass
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def page1(request):

    return render(request,'page1.html')
def page2(request):

    return render(request,'page2.html')
def page3(request):

    return render(request,'page3.html')
def page4(request):

    return render(request,'page4.html')
def page5(request):

    return render(request,'page5.html')
def page6(request):

    return render(request,'page6.html')
def page7(request):

    return render(request,'page7.html')
def faq(request):

    return render(request,'faq.html')

def load_model(request):
    with open('main/model/HateSpeechD_Model.pkl', 'rb') as f:
        model = pickle.load(f)
    return HttpResponse("Model loaded successfully!")

def results(request):
    return render(request,'results.html')
def Quotation1(request):
    return render(request,'Quotation1.html')

def Quotation2(request):
    return render(request,'Quotation2.html')

def Quotation3(request):

    return render(request,'Quotation3.html')


def consultation(request):

    return render(request,'consultation.html')
def design(request):

    return render(request,'ref1.html')

def installation(request):

    return render(request,'ref2.html')
def maintenance(request):

    return render(request,'ref3.html')
    
def ref4(request):

    return render(request,'ref4.html')
def page8(request):

    return render(request,'page8.html')
def page9(request):

    return render(request,'page9.html')


import pickle

def model(request):
    def predict(request):
    # load model from JSON file
     with open('model_params.json', 'r') as json_file:
        model_params = json.load(json_file)

    # create a new model with the loaded parameters
    loaded_model = joblib.load('HateSpeechD_Model.pkl')

    # load test data from request
    X_test = request.GET.getlist('x[]', [])
    X_test = [float(x) for x in X_test]

    # make prediction
    y_predict = loaded_model.predict([X_test])

    # return prediction as JSON
    return JsonResponse({'prediction': y_predict[0]})
    # Use the model to make predictions


