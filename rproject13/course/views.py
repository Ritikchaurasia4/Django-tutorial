from django.shortcuts import render

# Create your views here.
def learn_django(request):
    # return render(request,'course/course1.html',{'nm':'Django Django'})
        #  OR,
    # cname = 'Django'
    # duration = '4 months'
    # seats = 10
    # Django_details = {'nm':cname , 'du':duration , 'st':seats}
    # return render(request,'course/course1.html',context=Django_details)

    # django_details = {'nm':'Django is awesome , wow'}

    return render(request,'course/course1.html',{'nm':'django is awesome'})

    # return render(request,'course/course1.html',{'nm':False})