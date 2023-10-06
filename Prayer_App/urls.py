from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('prayers/', views.prayers, name='prayers'),
    path('videos/', views.videos, name='videos'),
    path('donation/', views.donation, name='donation'),
    path('process_donation/', views.process_donation, name='process_donation'),
    path('paypal-ipn/', views.process_donation, name='paypal-ipn'),
    path('donation_success/', views.donation_success, name='donation_success'),
    path('donation_cancel/', views.donation_cancel, name='donation_cancel'),
]
