from django.shortcuts import render
import requests

API_KEY = "b8bb286245f5d721119e604aeafbe1a9"

# Create your views here.


def home(request):
    if request.method == "POST":
        try:
            city = request.POST["city"]
        except KeyError:
            return render(request, "index.html", {"error": "Please enter a city name."})
        
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        if response.status_code == 200:
            response_data = response.json()
            try:
                data = {
                    "city_code": response_data["sys"]["country"],
                    "temperature": response_data["main"]["temp"],
                    "pressure": response_data["main"]["pressure"],
                    "humidity": response_data["main"]["humidity"],
                    "coordinates": response_data["coord"],
                    "city": city,
                    "imoji" : response_data["weather"][0]["icon"]
                }
            except KeyError as e:
                return render(request, "index.html", {"error": e})
            
            return render(request, "index.html", {"data": data})
        else:
            return render(request, "index.html", {"error": response.json()})
    return render(request, "index.html")

    