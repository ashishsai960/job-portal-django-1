from django.urls import path
from .views import JobRegistrationAPI, JobListAPI,JobDetailAPI,DocumentUploadAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register-jobs/', JobRegistrationAPI.as_view(), name='job'),
    path('jobs/', JobListAPI.as_view(), name='job-list'),
    path('<int:id>/', JobDetailAPI.as_view(), name='job_detail'),
    path('upload-documents/', DocumentUploadAPI.as_view(), name='upload-documents'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
