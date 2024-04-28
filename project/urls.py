from .views import Pricing , Home
from django.urls import path

urlpatterns = [
    path('pricing/' , Pricing.as_view() , name="pricing"),  # objectiv
    path('' , Home.as_view() , name="home"), 
]