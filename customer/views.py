from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'customer/customer_home.html')
def products(request):
    return render(request,'customer/customer_products.html')

def profile(request):
    return render(request,'customer/profile.html')
    
def payment(request):
    return render(request,'customer/payment.html')