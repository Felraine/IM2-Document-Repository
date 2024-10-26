from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings_view, name='settings'),  # Add this line
    path('dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),  # Your existing line
]
