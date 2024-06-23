

from django.shortcuts import render , redirect
from .serializers import JobRegistrationSerializer 
from rest_framework import generics, response, permissions
from .models import Job
from django.db.models import Q
from .pagination import CustomPagination
from .serializers import DocumentSerializer
class JobRegistrationAPI(generics.CreateAPIView):
    serializer_class = JobRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        job = serializer.save()
        return response.Response({
            "job": JobRegistrationSerializer(job, context=self.get_serializer_context()).data,
            "message": "Job registered successfully"
        })
    



class JobListAPI(generics.ListAPIView):
    serializer_class = JobRegistrationSerializer
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

class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobRegistrationSerializer
    lookup_field = 'id'
    

class DocumentUploadAPI(generics.CreateAPIView):
    serializer_class = DocumentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = serializer.save()
        return response.Response({
            "document": DocumentSerializer(document, context=self.get_serializer_context()).data,
            "message": "Documents uploaded successfully"
        })
   