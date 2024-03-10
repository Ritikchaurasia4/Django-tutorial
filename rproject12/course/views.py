from django.shortcuts import render

# Create your views here.
def learn_django(request):
    # coursename = {'cname':'django django'}
    cname = 'django'
    duration = '4 months'
    seats = 10
    django_details = {'nm':cname , 'du':duration , 'st':seats}
    return render(request,'course/course1.html',#context=coursename , 
                  django_details)
def learn_python(request):
    return render(request,'course/course2.html')