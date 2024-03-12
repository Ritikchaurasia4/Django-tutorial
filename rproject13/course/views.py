from django.shortcuts import render
# from datetime import datetime
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

    # return render(request,'course/course1.html',{'nm':'django is awesome'})

    # return render(request,'course/course1.html',{'nm':False})

    # d = datetime.now()
    # return render(request ,'course/course1.html',{'dt':d})

    return render(request,'course/course1.html',{'p1':56.23421 , 'p2':56.0000 , 'p3':56.370000})