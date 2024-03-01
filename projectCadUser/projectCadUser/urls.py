from django.urls import path
from app_CadUser import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # rafael.com
    path('', views.home, name='Home'),
    path('users/', views.users, name='list_users')
]
