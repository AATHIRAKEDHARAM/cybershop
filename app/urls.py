from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("", views.home, name="home"),
    path("product-detail/", views.product_detail, name="product-detail"),
    path("cart/", views.add_to_cart, name="add-to-cart"),
    path("buy/", views.buy_now, name="buy-now"),
    path("profile/", views.profile, name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("changepassword/", views.change_password, name="changepassword"),
    path("mobile/", views.mobile, name="mobile"),
    path("adminlogin/", views.adminlogin, name="adminlogin"),
    path("customerlogin/", views.customerlogin, name="customerlogin"),
    path("sellerlogin/", views.sellerlogin, name="sellerlogin"),
    path(
        "customerregistration/", views.customerregistration, name="customerregistration"
    ),
    path("sellerregistration/", views.sellerregistration, name="sellerregistration"),
    path("checkout/", views.checkout, name="checkout"),
]
