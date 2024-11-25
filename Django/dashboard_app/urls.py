from django.urls import path
from .views import dashboard_view, addEvent,deleteEvent, get_events,updateEvent

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  
    path('addEvent/', addEvent, name='addEvents'),
    path('delete/<int:event_id>/', deleteEvent, name='deleteEvent'),
    path('updateEvent', updateEvent, name='updateEvent'), 
    path('get_events/', get_events, name='get_events'),
]