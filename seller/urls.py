from django.urls import path
from .import views

app_name="seller"
urlpatterns = [
    path('', views.home, name="home"),
    path('addproduct/', views.addbook, name="add"),
     path('product/', views.product, name="product"),
     path('edit/', views.edit, name="edit"),
]