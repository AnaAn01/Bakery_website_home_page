from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('/cart/', views.cart, name='cart'),
]