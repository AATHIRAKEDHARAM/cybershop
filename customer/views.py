from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'customer/customer_home.html')
def products(request):
    return render(request,'customer/customer_products.html')