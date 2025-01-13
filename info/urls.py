from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contacts/', views.contact_list, name='contact_list'),
]
