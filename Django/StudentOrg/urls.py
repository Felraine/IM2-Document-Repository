from django.contrib import admin
from django.urls import path, include
from calendar_app.views import calendar_view  
from register_app.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register_app.urls')), #login/logout
    path('', register_view, name='register'), 
    
    path('calendar/', include('calendar_app.urls')),  
    path('calendar/', calendar_view, name='calendar'), 

    #path('',include("django.contrib.auth.urls")), # auth url for login/logout
]
