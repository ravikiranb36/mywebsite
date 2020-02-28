from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    for dest in dests:
        print(dest.img.url)

    return render(request, 'index.html', {'dests': dests})
def about(request):
    return render(request, 'about.html')
def news(request):
    return render(request, 'news.html')
def contact(request):
    return render(request, 'contact.html')