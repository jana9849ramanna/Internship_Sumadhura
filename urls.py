from django.urls import path
from . import views

urlpatterns = [
    path('vehicle-info/', views.vehicle_info, name='vehicle_info'),
    path('quality-check/<int:vehicle_id>/', views.quality_check, name='quality_check'),
    # Add other URLs as needed...
]
