from django.shortcuts import render, redirect

def diaries(request):
    return render(request, 'diaries/DIARIES.html')

def book_detail(request):
    return render(request, 'diaries/solitude.html')