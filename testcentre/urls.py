from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_test_centres, name='manage_test_centres'),
    path('delete/<int:pk>/', views.delete_test_centre, name='delete_test_centre'),
    path('edit/<int:pk>/', views.edit_test_centre, name='edit_test_centre'),
]
