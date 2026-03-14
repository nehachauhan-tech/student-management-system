from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('accounts/signup/', views.signup, name='signup'),
]

