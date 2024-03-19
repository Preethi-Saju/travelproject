from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


# Create your views here.


def demo(request):
    obj=Place.objects.all()
    objt=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':objt})
#def addition(request):
  #  x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #sub=x-y
    #div=x/y
    #product=x*y
    #return render(request,"result.html", {'result':res,'subtraction':sub,'division':div,'multiplication':product})
