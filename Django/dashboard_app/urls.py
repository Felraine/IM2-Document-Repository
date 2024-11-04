from django.urls import path
from .views import dashboard_view, addEvent

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  
    path('addEvent/', addEvent, name='addEvents'),
]
