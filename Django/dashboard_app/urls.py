from django.urls import path
from .views import dashboard_view, addEvent,deleteEvent, get_events,updateEvent,addTasks, get_tasks, addMeeting, deleteMeeting, updateMeeting, get_meeting

urlpatterns = [
    path('', dashboard_view, name='dashboard'),  
    path('addEvent/', addEvent, name='addEvents'),
    path('delete/<int:event_id>/', deleteEvent, name='deleteEvent'),
    path('updateEvent', updateEvent, name='updateEvent'), 
    path('get_events/', get_events, name='get_events'),
    path('addTasks/', addTasks, name='addTasks'),
    path('get_tasks/', get_tasks, name='getTask'),
    
    #meeting routes
    path('addMeeting/', addMeeting, name='addMeeting'),
    path('deleteMeeting/<int:meeting_id>/', deleteMeeting, name='deleteMeeting'),
    path('updateMeeting/<int:meeting_id>/', updateMeeting, name='updateMeeting'),
    path('get_meeting/', get_meeting, name='get_meeting'),
]