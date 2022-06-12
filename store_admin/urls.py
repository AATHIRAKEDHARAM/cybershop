from django.urls import path
from . import views

app_name = "store_admin"
urlpatterns = [
    path("dash/", views.dashboard, name="dash"),
    path("plist/", views.productlist, name="plist"),
    path("padd/", views.productadd, name="padd"),
    path("cat/", views.catlist, name="cat"),
    path("catadd/", views.catadd, name="catadd"),
    path("sell/", views.sellerlist, name="sell"),
    path("addsell/", views.addseller, name="addsell"),
    path("order/", views.orderlist, name="order"),
    path("order1/", views.orderdet, name="orderdet"),
]
