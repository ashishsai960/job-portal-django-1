from django.urls import path
from .views import JobSeekerRegisterView, JobHirerRegisterView, CustomTokenObtainPairView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/job-seeker/', JobSeekerRegisterView.as_view(), name='job_seeker_register'),
    path('register/job-hirer/', JobHirerRegisterView.as_view(), name='job_hirer_register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
