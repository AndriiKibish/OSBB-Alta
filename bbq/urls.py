from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'bbq'

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('all/', views.all_bookings, name='all_bookings'),
    path('future_bookings/', views.future_bookings, name='future_bookings'),
    path('<int:pk>/delete/', views.delete_booking, name='delete_booking'),
    path('success_bbq/', lambda request: render(request, 'bbq/success_bbq.html'), name='success_bbq'),
]
