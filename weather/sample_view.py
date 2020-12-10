from urllib.request import urlopen

import requests
from xml.etree import ElementTree as ET

def add(a, b):
    return a + b


def hourly_weather():
    try:
        url_2 = 'https://api.openweathermap.org/data/2.5/forecast?q={}&mode=xml&appid=3296c2619b03efacdefe1368d5f4ce41'

        # city_name = requests.get('city')
        # if not city_name:
        city_name = 'Kathmandu'

        r = requests.get(url_2.format(city_name)).text

        # print(r)
        #
        # root = ET.XML(r)
        # print(root)
        #
        # forecast = root[4]
        # print(forecast)
        #
        # first_three_forecast = forecast[1:3]
        # print(first_three_forecast)
        #
        # time_1 = first_three_forecast[0]
        # # print(time_1)
        # # print(time_1[4].attrib)
        # temp_dic = time_1[4].attrib
        # print(temp_dic['value'])
        # symbol_dic = time_1[0].attrib
        # print(symbol_dic['var'])
        #
        # time_2 = first_three_forecast[1]
        # # print(time_2)
        # temp_dic = time_2[4].attrib
        # print(temp_dic['value'])
        #
        # time_3 = first_three_forecast[2]
        # # print(time_3)
        # temp_dic = time_3[4].attrib
        # print(temp_dic['value'])

    except IndexError as ie:
        print(f'{city_name} not found')





hourly_weather()
