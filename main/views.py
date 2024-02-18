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
from .models import Home, EnergyReading, SolarReading


# Create your views here.
def main (request):

    return render(request, 'index.html')

def equipment(request):

    return render(request, 'extra/equipment.html')

def dashboard(request):

    return render(request, 'extra/user_dashboard.html')

def recommendations(request):

    return render(request, 'extra/tailored_recommendations.html')

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
            user = form.save()
            login(request, user)
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


def user_dashboard(request, home_id):
    home = Home.objects.get(id=home_id)
    energy_readings = EnergyReading.objects.filter(home=home).order_by('-timestamp')
    solar_readings = SolarReading.objects.filter(home=home).order_by('-timestamp')
    return render(request, 'user_ dashboard.html', {'home': home, 'energy_readings': energy_readings, 'solar_readings': solar_readings})


    