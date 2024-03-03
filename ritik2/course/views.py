from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse('hello ritik')
def learn_python(request):
    return HttpResponse('<h2>hello ritik </h2>')
def learn_var(request):
    a='<h1> hello ritik </h1>'
    return HttpResponse(a)
def learn_math(request):
    a=10+10
    return HttpResponse(a)
def index(request):
    return HttpResponse('Home page')