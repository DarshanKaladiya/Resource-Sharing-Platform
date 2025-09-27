from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    # Homepage URL
    path('', views.home, name='home'),
    
    # Core URLs
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('signup/', views.signup, name='signup'),

    # Dashboard URLs
    path('mentor_dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    
    # Course and Resource Management URLs
    path('create_course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/upload_resource/', views.upload_resource, name='upload_resource'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),

    # Advanced Feature URLs
    path('search/', views.search_results_view, name='search_results'),
    path('resource/<int:resource_id>/approve/', views.approve_resource, name='approve_resource'),
    path('resource/<int:resource_id>/reject/', views.reject_resource, name='reject_resource'),
    path('notifications/', views.notification_list, name='notification_list'),
    
    # URLs for Deleting Content
    path('resource/<int:resource_id>/delete/', views.delete_resource, name='delete_resource'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
]

