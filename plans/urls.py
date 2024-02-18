# urls.py
from django.urls import path
from .views import quotation

urlpatterns = [
    path('quotation/', quotation, name='quotation'),
   
]
