from django.urls import path
from .views import *
urlpatterns = [
    path('product/create/<name>', CreateProduct),
    path('product/get/<hash>', GetProduct),
    path('product/search/<query>', SearchProduct),
    path('image/upload/<hash>', UploadImage),
    path('image/display/<hash>', DisplayImage)
]
