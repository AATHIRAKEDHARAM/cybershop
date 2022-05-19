from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'seller/seller_home.html')
def addbook(request):
    return render(request,'seller/seller_add.html')
def product(request):
    return render(request,'seller/seller_product.html')
def edit(request):
    return render(request,'seller/seller_edit.html')
