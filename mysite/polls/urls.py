from django.urls import path
from . import views

urlpatterns=[
    path('info/', views.user_info, name="user_info"),
]