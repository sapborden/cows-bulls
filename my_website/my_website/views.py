from django.shortcuts import render

def welcome(request):
    return render(request, 'my_website/welcome.html')