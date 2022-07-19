import email
from django.shortcuts import redirect, render

from app.models import AdminLogin, CustomerReg, SellerRegistration


def home(request):
    return render(request, "app/home.html")


def product_detail(request):
    return render(request, "app/productdetail.html")


def add_to_cart(request):
    return render(request, "app/addtocart.html")


def buy_now(request):
    return render(request, "app/buynow.html")


def profile(request):
    return render(request, "app/profile.html")


def address(request):
    return render(request, "app/address.html")


def orders(request):
    return render(request, "app/orders.html")


def change_password(request):
    return render(request, "app/changepassword.html")


def mobile(request):
    return render(request, "app/mobile.html")


def adminlogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        admin_exist = AdminLogin.objects.filter(email=email, password=password).exists()
        if admin_exist:
            admin = AdminLogin.objects.get(email=email, password=password)
            request.session["admin_id"] = admin.id
            return redirect("store_admin:dash")
        else:
            msg = "invaild email or password"
            return render(
                request,
                "app/adminlogin.html",
                {
                    "error_msg": msg,
                },
            )

    return render(request, "app/adminlogin.html")


def customerlogin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user_exists=CustomerReg.objects.filter(email=email,password=password).exists()
        if user_exists:
            customer=CustomerReg.objects.get(email=email,password=password)
            request.session["customer _id"]=customer.id
            return redirect("customer:home")
        else:
            msg="invaild email or password"
            return render(request, "app/customerlogin.html",{"msg":msg})

    return render(request, "app/customerlogin.html")
    
   


def sellerlogin(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user_exist = SellerRegistration.objects.filter(
            email=email, password=password
        ).exists()

        if user_exist:
            seller = SellerRegistration.objects.get(email=email, password=password)
            request.session["user_id"] = seller.id
            return redirect("home")
        else:
            msg = "invaild email or password"
        return render(
            request,
            "app/sellerlogin.html",
            {
                "msg": msg,
            },
        )

    return render(request, "app/sellerlogin.html")


def customerregistration(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        customer_exists=CustomerReg.objects.filter(email=email).exists()
        if customer_exists:
            msg = "customer email already exists"
                
            return render(request, "app/customerregistration.html",{"msg":msg})
        
            
        else:
            customer=CustomerReg(email=email,password=password)
            customer.save()
            return redirect('app:customerlogin')
          
       
    return render(request, "app/customerregistration.html")


def sellerregistration(request):

    if request.method == "POST":
        acc_name = request.POST["acc_name"]
        acc_number = request.POST["acc_number"]
        branch = request.POST["branch"]
        ifsc = request.POST["ifsc"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        country = request.POST["country"]
        pin = request.POST["pin"]
        password = request.POST["password"]

        seller = SellerRegistration(
            acc_name=acc_name,
            acc_number=acc_number,
            branch=branch,
            ifsc=ifsc,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            country=country,
            pin=pin,
            password=password,
        )
        seller.save()

    return render(request, "app/sellerregistration.html")


def checkout(request):
    return render(request, "app/checkout.html")
