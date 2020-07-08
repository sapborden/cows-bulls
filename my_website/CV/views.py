from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'CV/about.html')