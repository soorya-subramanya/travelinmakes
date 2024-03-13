from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Mentors

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Mentors.objects.all()

    return render(request,"index.html",{'result':obj,'result2':obj1})








# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#
#     return render(request,"result.html",{'result1':add,'result2':sub,'result3':mul,'result4':div})




