from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    
    # Dashboard and Survey URLs
    path('dashboard-data/', views.dashboard_data, name='dashboard_data'),
    path('submit-survey/', views.submit_survey, name='submit_survey'),
    path('survey-stats/', views.get_survey_stats, name='survey_stats'),
    
    # About page data
    path('about-data/', views.about_data, name='about_data'),
    
    # Contact form
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    
    # Homepage statistics
    path('home-stats/', views.home_stats, name='home_stats'),
    
    # States list for forms
    path('get-states/', views.get_states, name='get_states'),
]