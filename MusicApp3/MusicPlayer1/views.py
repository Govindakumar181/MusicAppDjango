from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"MusicPlayer1/index.html")


def Govinda(request):
    return HttpResponse("Hello Govinda")

def greet(request,name):
    return render(request,'MusicPlayer1/greet.html',{
        "name": name.capitalize()
    })
    return HttpResponse(f"Hello {name.capitalize()}")



