from django.shortcuts import render


def home(request):
    import json
    import requests
    #http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=DC937C79-8B92-4099-B0A3-13226AAA32DA
    api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=DC937C79-8B92-4099-B0A3-13226AAA32DA')
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api' : api})


def about(request):
    return render(request, 'about.html', {})

def search(request):
    return render(request, 'search.html', {})

