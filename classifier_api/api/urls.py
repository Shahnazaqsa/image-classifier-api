from django.urls import path 
from .views import PredictDigits

urlpatterns = [
    path('predict/', PredictDigits.as_view() , name='predict-digit')
]
