from django.urls import path
from .views import dashboard_view, addEvent,deleteEvent, get_events,updateEvent,addTasks, get_tasks, addMeeting, deleteMeeting, updateMeeting, get_meeting,updateTask,deleteTask

urlpatterns = [
    path('', dashboard_view, name='dashboard'), 

    #events paths 
    path('addEvent/', addEvent, name='addEvents'),
    path('delete/<int:event_id>/', deleteEvent, name='deleteEvent'),
    path('updateEvent', updateEvent, name='updateEvent'), 
    path('get_events/', get_events, name='get_events'),

    #tasks paths
    path('addTasks/', addTasks, name='addTasks'),
    path('updateTask/', updateTask, name='updateTask'),
    path('get_tasks/', get_tasks, name='getTask'),
    path('delete-task/<int:task_id>/',deleteTask, name='deleteTask'),
    
    #meeting routes
    path('addMeeting/', addMeeting, name='addMeeting'),
    path('deleteMeeting/<int:meeting_id>/', deleteMeeting, name='deleteMeeting'),
    path('updateMeeting/<int:meeting_id>/', updateMeeting, name='updateMeeting'),
    path('get_meeting/', get_meeting, name='get_meeting'),
]