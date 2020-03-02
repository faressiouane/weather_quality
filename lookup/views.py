from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'person' : 'fares'})

def about(request):
    return render(request, 'about.html', {})

