# from django.urls import path
# from .views import JobRegistrationAPI, JobListAPI,JobDetailAPI,DocumentUploadAPI
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('register-jobs/', JobRegistrationAPI.as_view(), name='job'),
#     path('jobs/', JobListAPI.as_view(), name='job-list'),
#     path('<int:id>/', JobDetailAPI.as_view(), name='job_detail'),
#     path('upload-documents/', DocumentUploadAPI.as_view(), name='upload-documents'),
    
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path
# from .views import JobListView, JobDetailView, JobApplicationCreateView, JobApplicationListView

# urlpatterns = [
#     path('register-jobs/', JobListView.as_view(), name='job-list'),
#     path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
#     path('apply/', JobApplicationCreateView.as_view(), name='apply-job'),
#     path('my-applications/', JobApplicationListView.as_view(), name='my-applications'),
# ]

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    # JobSeekerRegisterView, JobHirerRegisterView, CustomTokenObtainPairView, ProfileView, 
    JobCreateView, JobListView, JobApplicationCreateView, JobApplicationListView, JobPostedListView
    # NotificationListView,
    
)

urlpatterns = [
    # path('register/job-seeker/', JobSeekerRegisterView.as_view(), name='job_seeker_register'),
    # path('register/job-hirer/', JobHirerRegisterView.as_view(), name='job_hirer_register'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/create/', JobCreateView.as_view(), name='job_create'),
    path('jobs/apply/', JobApplicationCreateView.as_view(), name='job_apply'),
    # path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('applications/', JobApplicationListView.as_view(), name='job-application-list'),
    path('posted-jobs/', JobPostedListView.as_view(), name='job-posted-list'),
]
