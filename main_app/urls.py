from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Jobs
    path('jobs/', views.JobList.as_view(), name='jobs_index'),
    path('jobs/<int:job_id>', views.jobs_detail, name='jobs_detail'),
    path('jobs/create/', views.JobCreate.as_view(), name='jobs_create'),
    path('jobs/<int:pk>/update/', views.JobUpdate.as_view(), name='jobs_update'),
    path('jobs/<int:pk>/delete/', views.JobDelete.as_view(), name='jobs_delete'),
    path('jobs/<int:job_id>/add_document/', views.add_document, name='add_document'),
    
    # Users
    path('accounts/sign/', views.signup, name='signup'),
]