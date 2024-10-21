from django.urls import path
from .views import JobSearchView, JobSearchDetailedView, JobSearchBySkillView, JobSearchByTitleView  # Import the new view

urlpatterns = [
     path('', home, name='home'),
    path('api/job-search/', JobSearchView.as_view(), name='job-search'),
    path('api/job-search-detailed/', JobSearchDetailedView.as_view(), name='job-search-detailed'),
    path('api/job-search-by-skill/', JobSearchBySkillView.as_view(), name='job_search_by_skill'),
    path('api/job-search-by-title/', JobSearchByTitleView.as_view(), name='job_search_by_title'),  # Add the new endpoint
]
