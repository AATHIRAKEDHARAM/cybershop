from django.urls import path
from .import views

app_name='customer'
urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('profile/', views.profile, name="profile"),
    path('payment/', views.payment, name="payment"),
    
]