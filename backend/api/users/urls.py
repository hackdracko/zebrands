from rest_framework.routers import DefaultRouter
from django.urls import path
from users import views
from users.views.user import UsersModelViewSet

from . import views

urlpatterns = [
    path('register', views.register),
    path('token', views.token),
    path('token/refresh', views.refresh_token),
    path('token/revoke', views.revoke_token),
]

router_user = DefaultRouter()

router_user.register(prefix='users', basename='users', viewset=UsersModelViewSet)