from django.urls import path, include
from .views import (
    frist_view, main_view,
    register, login_view, exit,
)

urlpatterns = [
    path('', frist_view, name='frist_view'),
    path('main/', main_view, name='main'),
    path('index/', frist_view, name='index'),
    path('logout/', exit, name='logout'),
    path('register/', register, name='register'),   
    path('login/', login_view, name='login'),
]
