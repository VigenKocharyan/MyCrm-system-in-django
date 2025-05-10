from rest_framework import serializers
from .models import Client, Task

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'status']

class TaskSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    class Meta:
        model = Task
        fields = ['id', 'client', 'title', 'description', 'due_date']
