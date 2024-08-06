from django.urls import path
from .views import index, brendha, raquel

urlpatterns = [
    path('brendha/', brendha, name='brendha'),
    path('raquel/', raquel, name='raquel'),
    path('', index, name='index')
]