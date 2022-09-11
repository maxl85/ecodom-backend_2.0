from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(parent__isnull=True)
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

