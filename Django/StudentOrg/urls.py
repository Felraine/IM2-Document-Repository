from django.contrib import admin
from django.urls import path, include
from calendar_app.views import calendar_view  
from register_app.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register_app.urls')),  
    path('', login_view, name='register'),  
    path('calendar/', include('calendar_app.urls')),
    path('dashboard/', include('dashboard_app.urls')),
    path('members/', include('members_app.urls')),  
]
