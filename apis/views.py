from django.shortcuts import render



# Create your views here.
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=84070&distance=50&API_KEY=1C27F481-552D-4922-BDE4-211DBC9A89C0
def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=84070&distance=50&API_KEY=1C27F481-552D-4922-BDE4-211DBC9A89C0")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error....."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
