from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="accounts-home"),
    path('register_customer/', views.register_customer, name="accounts-register-customer"),
    path('register_staff/', views.register_staff, name="accounts-register-staff"),

    path('login_user/', views.login_user, name="accounts-login-user"),
    path('logout_user/', views.logout_user, name="accounts-logout-user"),

    path('profile_customer/<int:pk>/', views.profile_customer, name="accounts-profile-customer"),
    path('update_customer/<int:pk>/', views.update_customer, name="accounts-update-customer"),
    path('delete_customer/<int:pk>/', views.delete_customer, name="accounts-delete-customer"),

    path('profile_staff/<int:pk>/', views.profile_staff, name="accounts-profile-staff"),
    path('update_staff/<int:pk>/', views.update_staff, name="accounts-update-staff"),
    path('delete_staff/<int:pk>/', views.delete_staff, name="accounts-delete-staff"),

    path('create_application/<int:pk>/', views.create_application, name="accounts-create-application"),
    path('read_application/<int:pk>/', views.read_application, name="accounts-read-application"),
    path('update_application/<int:pk>/', views.update_application, name="accounts-update-application"),
    path('delete_application/<int:pk>/', views.delete_application, name="accounts-delete-application"),
]
