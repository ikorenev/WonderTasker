
import urllib.request
import json


source = urllib.request.urlopen(
    'http://api.openweathermap.org/data/2.5/weather?q=Rostov-on-Don&units=metric&appid=a15417c7ebe0bcce38f2aabdd96f2549').read()

# convert  json file into python dectionary
list_of_data = json.loads(source)

data = {
    'temp': str(list_of_data["main"]['temp']),
    'feels_temp': str(list_of_data["main"]['feels_like']),
    'pressure': str(list_of_data['main']["pressure"]),
    'humidity': str(list_of_data['main']['humidity'])
}

weather=f"Погода в Ростове-на-Дону:\nТемпература: {data['temp']}\nОщущается как: {data['feels_temp']}\nДавление: {data['pressure']}\nВлажность: {data['humidity']}"

def getURL(anim):

    link = json.loads(urllib.request.urlopen(f'https://some-random-api.ml/animal/{anim}').read())
    url = str(link['image'])
    return url

