from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, "website/index.html")