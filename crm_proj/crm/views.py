from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from .models import Client, Task
from .forms import ClientForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientSerializer, TaskSerializer

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created successfully.')
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'crm/client_form.html', {'form': form})
@login_required
def client_list(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    sort_by = request.GET.get('sort_by', 'name')  # По умолчанию сортировка по имени
    order = request.GET.get('order', 'asc')  # Сортировка по возрастанию или убыванию

    # Получаем клиентов с фильтрами
    clients = Client.objects.all()

    if query:
        clients = clients.filter(name__icontains=query)
    if status:
        clients = clients.filter(status=status)

    # Сортировка по имени или email
    if order == 'asc':
        clients = clients.order_by(sort_by)  # По возрастанию
    else:
        clients = clients.order_by(f'-{sort_by}')  # По убыванию

    # Пагинация
    paginator = Paginator(clients, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'crm/client_list.html', {
        'page_obj': page_obj,
        'query': query,
        'status': status,
        'sort_by': sort_by,
        'order': order,
    })
    
@login_required    
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'crm/client_detail.html', {'client': client})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully.')
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'crm/client_form.html', {'form': form, 'client': client})
@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully.')
        return redirect('client_list')
    return render(request, 'crm/client_confirm_delete.html', {'client': client})

@login_required
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'crm/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task_list')
    else:
        task_form = TaskForm()
    return render(request, 'crm/add_task.html', {'form': task_form})

class LogoutView(LogoutView):
    
    http_method_names = ['get', 'post']
    next_page = 'login'
    
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-due_date')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]