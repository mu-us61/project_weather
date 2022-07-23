from django.shortcuts import render, redirect
import json
import urllib.request

# Create your views here.


def index_view(request):
    myapi = "fbb3d5c163421bd74fce7b9bafaed10e"
    if request.method == "GET":
        return render(request, template_name="app_base/index.html")
    if request.method == "POST":
        city = request.POST["city"]
        # source = urllib.request.urlopen(
        #     'http://api.openweathermap.org/data/2.5/weather?q ='
        #             + city + '&appid = your_api_key_here').read()
        source = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid="
            + myapi
            + "&units=metric"
        ).read()
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        # data for variable list_of_data
        print(list_of_data)
        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "coordinate": str(list_of_data["coord"]["lon"])
            + " "
            + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]) + " derece",
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "name": str(list_of_data["name"]),
        }
        print(data)
        # return redirect("app_base:index_view_name")
        return render(request, template_name="app_base/index.html", context=data)
