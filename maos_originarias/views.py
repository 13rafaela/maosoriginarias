from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("esta é a tela inicial do app")
def login(request):
    return HttpResponse("esta é a tela de login do app")
def produto(request):
    return HttpResponse("esta é a tela do produto do app")