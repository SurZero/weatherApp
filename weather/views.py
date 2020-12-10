# from os import truncate
# from urllib.request import urlopen
# from .forms import CityForm
# from .models import City
import xml.etree.ElementTree as ET
from django.shortcuts import render
import requests
from django.contrib import messages


def get_current_weather(city_name, weather):
    return {
        'city': city_name,
        'temperature': format((weather['main']['temp'] - 273.15), '.1f'),
        'min_temperature': format((weather['main']['temp_min'] - 273.15), '.1f'),
        'max_temperature': format((weather['main']['temp_max'] - 273.15), '.1f'),
        'humidity': weather['main']['humidity'],
        'wind': weather['wind']['speed'],
        'icon': weather['weather'][0]['icon'],
    }


def current_weather(request):
    url_1 = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=3296c2619b03efacdefe1368d5f4ce41'
    # print(request.POST.get('city'))
    # city_name = ''
    try:
        city_name = request.POST.get('city') or request.GET.get('city', None)
        if not city_name:
            city_name = 'Kathmandu'
        # print(request.POST.get('city'))
        r = requests.get(url_1.format(city_name)).json()

        current_weather = get_current_weather(city_name, r)
        return current_weather

    except KeyError as er:

        # print(f'{city_name} not found!')
        messages.error(request, f'city named {city_name} not found!')
        city_name = 'Kathmandu'
        r = requests.get(url_1.format(city_name)).json()

        current_weather = get_current_weather(city_name, r)
        return current_weather


def get_hourly_weather(r, city_name):
    root = ET.XML(r)
    # print(root.tag)

    forecast = root[4]
    # print(forecast.tag)

    first_three_forecast = forecast[1:4]
    # print(first_three_forecast)

    time_1 = first_three_forecast[0]
    # print(time_1)
    # print(time_1[4].attrib)
    temp_dic = time_1[4].attrib
    temperature_1 = temp_dic['value']

    symbol_dic = time_1[0].attrib
    icon_1 = symbol_dic['var']

    time_2 = first_three_forecast[1]
    # print(time_2)
    temp_dic = time_2[4].attrib
    temperature_2 = temp_dic['value']
    symbol_dic = time_2[0].attrib
    icon_2 = symbol_dic['var']

    time_3 = first_three_forecast[2]
    # print(time_3)
    temp_dic = time_3[4].attrib
    temperature_3 = temp_dic['value']
    symbol_dic = time_3[0].attrib
    icon_3 = symbol_dic['var']

    print(icon_3)
    print(temperature_3)

    hourly_weather = {
        'temperature_1': format(float(temperature_1) - 273.15, '.1f'),
        'icon_1': icon_1,
        'temperature_2': format(float(temperature_2) - 273.15, '.1f'),
        'icon_2': icon_2,
        'temperature_3': format(float(temperature_3) - 273.15, '.1f'),
        'icon_3': icon_3,
    }

    return hourly_weather


def hourly_weather(request):
    url_2 = 'https://api.openweathermap.org/data/2.5/forecast?q={}&mode=xml&appid=3296c2619b03efacdefe1368d5f4ce41'

    try:
        city_name = request.POST.get('city')
        if not city_name:
            city_name = 'Kathmandu'
        r = requests.get(url_2.format(city_name)).text

        hourly_weather = get_hourly_weather(r, city_name)
        return hourly_weather

    except IndexError as ke:
        print(f'city named {city_name} not found')
        city_name = 'Kathmandu'
        r = requests.get(url_2.format(city_name)).text
        hourly_weather = get_hourly_weather(r, city_name)
        return hourly_weather


def home(request):
    context = {'current_weather': current_weather(request),
               'hourly_weather': hourly_weather(request),
               }

    if request.POST and request.POST.get('city'):
        context.update({"city": request.POST.get('city')})
    return render(request, 'weather/home.html', context)


def weekly(request):
    context = {'current_weather': current_weather(request)}
    return render(request, 'weather/weekly.html', context)
