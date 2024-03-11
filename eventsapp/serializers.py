from rest_framework import serializers
from . import models

class event_serializer(serializers.ModelSerializer):
  
    class Meta:
      model = models.Event
      fields = '__all__'

