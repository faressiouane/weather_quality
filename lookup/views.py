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

    if api[0]["Category"]["Name"] == "Good":
        color = "green"
        msg = "Air quality is considered satisfactory, and air pollution poses little or no risk."

    elif api[0]["Category"]["Name"] == "Moderate":
        color = "yelow"
        msg = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."

    elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
        color = "orange"
        msg = "Members of sensitive groups may experience health effects. The general public is not likely to be affected. "

    elif api[0]["Category"]["Name"] == "Unhealthy":
        color = "red"
        msg = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."

    elif api[0]["Category"]["Name"] == "Very Unhealthy":
        color = "purple"
        msg = "Health alert: everyone may experience more serious health effects."

    else:
        color = "deep-purple darken-4"
        msg = "Health warnings of emergency conditions. The entire population is more likely to be affected."
    
  


    return render(request, 'home.html', {'api' : api, 'color' : color, 'msg' : msg})


def about(request):
    return render(request, 'about.html', {})

def search(request):
    return render(request, 'search.html', {})

