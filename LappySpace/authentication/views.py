from django.shortcuts import render,HttpResponse
# Create your views here.
def register(request):
    return HttpResponse("Register Page")
def login(request):
    return HttpResponse("login Page")