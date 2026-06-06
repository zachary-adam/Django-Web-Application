from django.urls import path
from . import views

app_name = 'DataEntry'

urlpatterns = [
    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Home and data entry
    path('', views.home_view, name='home'),
    
    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('profile/change-password/', views.change_password_view, name='change_password'),
    
    # Entity management
    path('entity/<int:pk>/', views.entity_detail_view, name='entity_detail'),
    path('entity/<int:pk>/delete/', views.entity_delete_view, name='entity_delete'),
]
