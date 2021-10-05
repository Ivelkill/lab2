from django.shortcuts import render
from django import template
# from django.http import HttpResponse


def home(request):
    return render(request, 'templates/static_handler.html')

# def home(request):
#     return render(request, 'templates/index.html')

# def home(request):
#     return HttpResponse('Привет, Мир!')
