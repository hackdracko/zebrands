from django.urls import path
from users import views

from . import views

urlpatterns = [
    path('register', views.register),
    path('token', views.token),
    path('token/refresh', views.refresh_token),
    path('token/revoke', views.revoke_token),
]