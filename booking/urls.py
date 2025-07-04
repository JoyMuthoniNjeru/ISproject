from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
    path('payment/<int:booking_id>/', views.payment_page, name='payment_page'),
    path('payment-success/', views.payment_success, name='payment_success'),

]
