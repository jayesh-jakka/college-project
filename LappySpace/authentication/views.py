from django.shortcuts import render,HttpResponse
from .models import CustomerDetails
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    context = {
        "saved" : False,
        "user-exist" : False
    }
    if request.method=="POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            customer_details = CustomerDetails.objects.create(user = user,customer_name = name,address=address,phone=contact)
            customer_details.save()
            context["saved"] = True
        except Exception as e:
            context["user-exist"] = True
        
        print(context["saved"])
    return render(request,"registration.html",context)
def login(request):
    return render(request,"login.html")