from django.shortcuts import render
from . import views
# Create your views here.
def fees_django(request):
    return render(request,'fees/fees1.html',{'title':'djangofee','cname':'django','charge':300})