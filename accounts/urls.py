from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products', views.products, name="products"),
    path('customer/<str:pk_tests>/', views.customer, "customer"),

    path('create_order/', views.createOrder, "create_order"),
]
