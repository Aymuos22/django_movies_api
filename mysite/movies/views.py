from django.shortcuts import render
from .serializers import Movieserializer
from rest_framework import viewsets
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=Movieserializer
