from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_page, name='auth'),  # one-page login/signup
]
