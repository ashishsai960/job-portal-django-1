

# from django.shortcuts import render , redirect
# from .serializers import JobRegistrationSerializer 
# from rest_framework import generics, response, permissions
# from .models import Job
# from django.db.models import Q
# from .pagination import CustomPagination
# from .serializers import DocumentSerializer
# class JobRegistrationAPI(generics.CreateAPIView):
#     serializer_class = JobRegistrationSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         job = serializer.save()
#         return response.Response({
#             "job": JobRegistrationSerializer(job, context=self.get_serializer_context()).data,
#             "message": "Job registered successfully"
#         })
    



# class JobListAPI(generics.ListAPIView):
#     serializer_class = JobRegistrationSerializer
#     pagination_class = CustomPagination

#     def get_queryset(self):
#         queryset = Job.objects.all()

#         print(self.request.query_params)

#         # Filtering by position
#         position = self.request.query_params.get('position', None)
#         if position:
#             queryset = queryset.filter(position__icontains=position)
        
#         tags = self.request.query_params.get('tags', None)
#         if tags:
#             queryset = queryset.filter(tags__icontains=tags)
        

#         location = self.request.query_params.get('location', None)
#         if location:
#             queryset = queryset.filter(location_restriction__icontains=location)


#         search_query = self.request.query_params.get('search', None)
#         if search_query:
#             queryset = queryset.filter(
#                 Q(position__icontains=search_query) | Q(
#                     tags__icontains=search_query)
#             )

#         salary_min = self.request.query_params.get('salary_min', None)
#         salary_max = self.request.query_params.get('salary_max', None)
#         if salary_min and salary_max:
#             queryset = queryset.filter(
#                 Q(annual_salary_min__gte=salary_min) & Q(annual_salary_max__lte=salary_max)
#             )
#         elif salary_min:
#             queryset = queryset.filter(annual_salary_min__gte=salary_min)
#         elif salary_max:
#             queryset = queryset.filter(annual_salary_max__lte=salary_max)

#         sort_by = self.request.query_params.get('sort_by', None)
#         sort_mapping = {
#             'latest': '-created_at',
#             'highest_salary': '-annual_salary_max',
#         }

#         if sort_by:
#             queryset = queryset.order_by(sort_mapping[sort_by])

#         return queryset

# class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobRegistrationSerializer
#     lookup_field = 'id'
    

# class DocumentUploadAPI(generics.CreateAPIView):
#     serializer_class = DocumentSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         document = serializer.save()
#         return response.Response({
#             "document": DocumentSerializer(document, context=self.get_serializer_context()).data,
#             "message": "Documents uploaded successfully"
#         })
    



   
# from rest_framework import generics, permissions, filters
# from rest_framework.pagination import PageNumberPagination
# from .models import Job, JobApplication
# from .serializers import JobSerializer, JobApplicationSerializer

# class JobPagination(PageNumberPagination):
#     page_size = 10

# class JobListView(generics.ListCreateAPIView):
#     queryset = Job.objects.all().order_by('-created_at')
#     serializer_class = JobSerializer
#     pagination_class = JobPagination
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['position', 'company_name', 'tags', 'location_restriction']

#     def perform_create(self, serializer):
#         serializer.save(posted_by=self.request.user)

# class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         job = self.get_object()
#         if job.posted_by != self.request.user:
#             raise permissions.PermissionDenied("You are not allowed to update this job")
#         serializer.save()

#     def perform_destroy(self, instance):
#         if instance.posted_by != self.request.user:
#             raise permissions.PermissionDenied("You are not allowed to delete this job")
#         instance.delete()

# class JobApplicationCreateView(generics.CreateAPIView):
#     serializer_class = JobApplicationSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class JobApplicationListView(generics.ListAPIView):
#     serializer_class = JobApplicationSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return JobApplication.objects.filter(applicant=self.request.user)


from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .models import Job, JobApplication
# , Notification
from .serializers import (
    JobSerializer,
    JobApplicationSerializer,
    # NotificationSerializer
)
from django.db.models import Q
from .pagination import CustomPagination

class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = JobSerializer
    

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class JobListView(generics.ListAPIView):
    # queryset = Job.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JobSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Job.objects.all()

        print(self.request.query_params)

        # Filtering by position
        position = self.request.query_params.get('position', None)
        if position:
            queryset = queryset.filter(position__icontains=position)
        
        tags = self.request.query_params.get('tags', None)
        if tags:
            queryset = queryset.filter(tags__icontains=tags)
        

        location = self.request.query_params.get('location', None)
        if location:
            queryset = queryset.filter(location_restriction__icontains=location)


        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(position__icontains=search_query) | Q(
                    tags__icontains=search_query)
            )

        salary_min = self.request.query_params.get('salary_min', None)
        salary_max = self.request.query_params.get('salary_max', None)
        if salary_min and salary_max:
            queryset = queryset.filter(
                Q(annual_salary_min__gte=salary_min) & Q(annual_salary_max__lte=salary_max)
            )
        elif salary_min:
            queryset = queryset.filter(annual_salary_min__gte=salary_min)
        elif salary_max:
            queryset = queryset.filter(annual_salary_max__lte=salary_max)

        sort_by = self.request.query_params.get('sort_by', None)
        sort_mapping = {
            'latest': '-created_at',
            'highest_salary': '-annual_salary_max',
        }

        if sort_by:
            queryset = queryset.order_by(sort_mapping[sort_by])

        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

# class NotificationListView(generics.ListAPIView):
#     queryset = Notification.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = NotificationSerializer

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

class JobApplicationListView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.account_type == 'job_hirer':
            return JobApplication.objects.filter(job__posted_by=user)
        return JobApplication.objects.none()

class JobPostedListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.account_type == 'job_hirer':
            return Job.objects.filter(posted_by=user)
        return Job.objects.none()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
