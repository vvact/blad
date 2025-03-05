from django.contrib import admin
from django.urls import path, include
from jobs import views as job_views  # import home view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/', views.job_list, name='job_list'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
