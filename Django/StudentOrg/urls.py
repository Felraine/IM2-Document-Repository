from django.contrib import admin
from django.urls import path, include
from calendar_app.views import calendar_view  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', include('calendar_app.urls')),  
    path('', calendar_view, name='home'), 
]
