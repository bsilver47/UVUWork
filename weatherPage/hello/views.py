from django.http import HttpResponse
from django.shortcuts import render
import requests
from munch import DefaultMunch
from django.contrib.syndication.views import Feed
from django.urls import reverse
from xml.dom.minidom import parse, parseString

## This receives the data from the weather API and adapts it to a usable format
response = requests.get("https://api.weather.gov/gridpoints/SLC/103,150/forecast/hourly")
jsonJson = DefaultMunch.fromDict(response.json())
periods = jsonJson.properties.periods

## This takes that usable data and puts it into variables and arrays to send to the HTML file
temp = "The Temperature in Orem is currently " + str(periods[0].temperature) + str(periods[0].temperatureUnit)
wind = " with winds of " + str(periods[0].windSpeed)
precip = " and a " + str(periods[0].probabilityOfPrecipitation.value) + "% chance of precipitation."
addWeather=[]
for period in range(1,13):
    weather = str(periods[period].temperature) + str(periods[period].temperatureUnit)
    time = ((periods[period].startTime).split("T"))[1]
    time = ((time.split("-"))[0])[:5]
    addWeather.append(time + " - " + weather)
iconUrl = (periods[0].icon).split(",")[0]

## As suggested by the variable names, this sets as a string the name of the color that will be used, dependent upon time of day as indicated by the weather api
if iconUrl.find("night") != -1:
    txtColor = "white"
else:
    txtColor = "black"

# rssfeed = requests.get("https://uvu.statuspage.io/history.rss")
# class rssFeed():
#     title =
# # https://realpython.com/python-xml-parser/
# # Please see above link for more info:
# # I didn't have time to finish reading




## These declared functions enable the variables to be read by other files
# Create your views here.
def index(request):
    return render(request, "hello/index.html", {
        "favicon_url": "https://www.uvu.edu/_common/images/uvu-mono.svg",
    })

def silver(request):
    return HttpResponse("Hello, Silver!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
        "favicon_url": "https://www.uvu.edu/_common/images/uvu-mono.svg",
        "weather_readout": (temp + wind + precip),
        "icon_url": iconUrl,
        "text_color": txtColor,
        "add_weather": addWeather,
        "weather_url": "https://forecast.weather.gov/MapClick.php?lat=40.2778058&lon=-111.7285704",
    })

## For additional help, please see one of the following two links:
## https://www.youtube.com/watch?v=w8q0C-C1js4
## https://www.w3schools.com/django/index.php
