from django.shortcuts import render

def diaries(request):
    return render(request, 'diaries/DIARIES.html')
