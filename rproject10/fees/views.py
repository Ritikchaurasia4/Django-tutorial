from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return render(request , 'course1.htm')
def fees_python(request):
    return render(request , 'course2.html')
def something(request):
    return HttpResponse('jai shree Ram')