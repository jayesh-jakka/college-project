from django.shortcuts import render

# Create your views here.
def serviceBooking(request):
    return render(request,'service.html')