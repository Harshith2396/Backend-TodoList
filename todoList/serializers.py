from rest_framework import serializers
from .models import tasks
class task_serialze(serializers.ModelSerializer):
    class Meta:
        model=tasks
        fields='__all__'