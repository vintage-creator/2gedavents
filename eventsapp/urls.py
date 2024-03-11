from django.urls import path
from .views import EventListCreateAPIView, EventRetrieveUpdateAPIView

urlpatterns = [
    path('api/events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateAPIView.as_view(), name='event-retrieve-update'),
]