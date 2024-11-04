from django.urls import path
from .views import members_view

urlpatterns = [
    path('', members_view, name='members'),  # URL for viewing members
]
