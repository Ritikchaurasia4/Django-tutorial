from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# here we also use render and HttpResponse with eachother

def learn_django(request):
    return render('<h1> hello django </h1>')
def learn_python(request):
    return HttpResponse('<h1> hello python </h1>')