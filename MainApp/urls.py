from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('skills/create/', views.create_skill, name='create_skill'),
    path('skills/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skills/<int:pk>/edit/', views.update_skill, name='update_skill'),
    path('skills/<int:pk>/delete/', views.delete_skill, name='delete_skill'),
    path('skills/<int:pk>/review/', views.add_review, name='add_review'),
    path('skills/<int:pk>/request/', views.send_booking_request, name='send_booking_request'),
]
