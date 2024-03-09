from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# here we also use render and HttpResponse with eachother

def learn_django(request):
    return render(request , 'course1.htm')
def learn_python(request):
    return render(request , 'course2.html')
def something(request):
    return HttpResponse('jai shree Ram')