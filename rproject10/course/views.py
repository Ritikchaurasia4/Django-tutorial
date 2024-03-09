from django.shortcuts import render


# Create your views here.

# here we also use render and HttpResponse with eachother

def learn_django(request):
    return render(request ,'course1.html')
def learn_python(request):
    return render(request ,'course2.html')

    