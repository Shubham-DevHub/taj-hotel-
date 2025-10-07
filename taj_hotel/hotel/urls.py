from django.urls import path 
from hotel import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('book/', views.book_room, name='book_room'),
    path('booking/', views.book_room, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
