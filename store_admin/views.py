from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'admin/adminhome.html')
def dashboard(request):
    return render(request,'admin/admindash.html')
def productlist(request):
    return render(request,'admin/productlist.html')
def productadd(request):
    return render(request,'admin/productadd.html')
def catlist(request):
    return render(request,'admin/categorylist.html')
def catadd(request):
    return render(request,'admin/categoryadd.html')
def sellerlist(request):
    return render(request,'admin/seller.html')
def addseller(request):
    return render(request,'admin/addseller.html')

def orderlist(request):
    return render(request,'admin/orderlist.html')
def orderdet(request):
    return render(request,'admin/orderdetails.html') 