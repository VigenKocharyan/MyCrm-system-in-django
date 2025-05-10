from django import forms
from .models import Client, Task  # Не забудь импортировать Task!

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone',]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['client', 'title', 'description', 'due_date', ]
