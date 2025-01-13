from django.shortcuts import render
from django.urls import path
from .views import submit_meter_reading, user_meter_readings

app_name = 'meters'

urlpatterns = [
    path('submit/', submit_meter_reading, name='submit_meter_reading'),
    path('success/', lambda request: render(request, 'meters/success.html'), name='meter_success'),
    path('my-readings/', user_meter_readings, name='user_readings')
]
