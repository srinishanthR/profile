from django.http import HttpResponse
from django.shortcuts import render
from . models import place
# Create your views here.
# PASSING VALUE FROM ONE PAGE TO ANOTHER
# def demo1(request):
#     name='india'
#     return render(request,'home.html',{'obj':name})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})

# STATIC WEBSITE
# def static(request):
#     return render(request,'index.html')
# CALLING OBJECTS
def demo(request):
    obj=place.objects.all()
    return render(request,'index.html',{'result':obj})