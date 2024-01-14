"""
URL mappings for the user API.
"""

from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateUserTokenView.as_view(), name='token'),
]
