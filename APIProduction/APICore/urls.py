from django.urls import path
from .views import *
urlpatterns = [
    path('product/create/<name>', CreateProduct),
    path('product/get/<hash>', GetProduct),
    path('image/store/<name>', StoreImage),
    path('image/display/<name>', DisplayImage),
]
