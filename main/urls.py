from django.urls import path
from main import views



urlpatterns = [
    path('',views.login_view , name='login'),
    path('register/', views.register_view, name='register'),

    path('main/', views.main, name='main'),
    path('equipment/', views.equipment, name='equipment'),

    path('tailored_recommendations/', views.recommendations, name='tailored_recommendations'),
    path('prediction/', views.prediction, name='prediction'),
    path('user_dashboard/',views.user_dashboard,   name='user_dashboard'),
]