from django.urls import path
from .views import dashboard_view, addEvent,deleteEvent

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  
    path('addEvent/', addEvent, name='addEvents'),
    path('delete/<int:event_id>/', deleteEvent, name='deleteEvent'),
]
