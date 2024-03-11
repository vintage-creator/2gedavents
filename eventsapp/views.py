from django.shortcuts import render
from rest_framework import generics
from .models import Event
from .permissions import CustomPermission
from .serializers import event_serializer

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = event_serializer
    permission_classes = [CustomPermission]

class EventRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = event_serializer
    permission_classes = [CustomPermission]