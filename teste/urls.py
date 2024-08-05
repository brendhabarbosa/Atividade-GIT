from django.urls import path
from .views import brendha

urlpatterns = [
    path('brendha/', brendha, name='brendha')
]