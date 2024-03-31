from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'fees/fees1.html',{'title':'Django fees','cname':'Django','charge':300})