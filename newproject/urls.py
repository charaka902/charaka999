from django.urls import path, include

urlpatterns = [
    path('jobs/', include('jobs.urls')),
]
