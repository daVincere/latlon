from django.shortcuts import render

from .models import SampleData
from .serializers import SampleSerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import generics 



class DataListing(generics.ListCreateAPIView):
	queryset = SampleData.objects.all()
	serializer_class = SampleSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SampleData.objects.all()
	serializer_class = SampleSerializer