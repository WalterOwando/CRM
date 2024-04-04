from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    # path('login/', views.login_user, name='login'),  # Uncomment if you have a login page
    path('logout/', views.logout_user, name='logout'),  # Logout
    path('register/', views.register_user, name='register'),  # User registration
    path('record/<int:pk>/', views.customer_record, name='record'),  # View customer record
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),  # Delete customer record
    path('add_record/', views.add_record, name='add_record'),  # Add new customer record
    path('update_record/<int:pk>/', views.update_record, name='update_record'),  # Update customer record
]
