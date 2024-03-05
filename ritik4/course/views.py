from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse('Hello ritik Rahul')

def learn_python(request):
    return HttpResponse('<h1>Hello python</h2>')

def learn_variable(request):
    a = '<h2> Hello variable </h2>'
    return HttpResponse(a)

    
def learn_math(request):
    a = 20+20
    return HttpResponse(a)

def learn_Name(request):
    a = 'Ritik and Rahul are brother'
    return HttpResponse(a)
