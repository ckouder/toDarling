from django.shortcuts import render
from .models import IwantToSay

# Create your views here.
def initialize(request):
    package = IwantToSay.objects.get(id=1)
    title = package.title
    words = package.words
    animate = package.animate

    return render(request, 'preparation/index.html', {
        'title': title, 
        'words': words, 
        'animate': animate,
    })