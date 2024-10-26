from django.contrib import admin
from django.urls import path, include
from calendar_app.views import calendar_view  
from register_app.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register_app.urls')),  # Login/logout
    path('', register_view, name='register'),  # Landing page for registration
    path('calendar/', include('calendar_app.urls')),  
    path('settings/', include('settings_app.urls')),  # This line includes settings_app urls
]
