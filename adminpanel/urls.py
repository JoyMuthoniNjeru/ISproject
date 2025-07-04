from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit/<int:pk>/', views.edit_slot, name='edit_slot'),
    path('delete/<int:pk>/', views.delete_slot, name='delete_slot'),
    path('confirmed-bookings/', views.confirmed_bookings_view, name='confirmed_bookings'),
    path('slot-config/', views.slot_config_view, name='slot_config'),
]
