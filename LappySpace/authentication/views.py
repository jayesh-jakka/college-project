from django.shortcuts import render,HttpResponse
# Create your views here.
def register(request):
    return render(request,"registration.html")
def login(request):
    return render(request,"login.html")