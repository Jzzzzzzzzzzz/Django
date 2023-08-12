from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisements



def index(request):
    advertisements = Advertisements.objects.all()
    contex = {"advertisements":advertisements}
    return render(request,'index.html',contex)

def top_sellers(request):
   return render(request,"top-sellers.html")

