from django.urls import path
from .views import home, dashboard, exit, register

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
