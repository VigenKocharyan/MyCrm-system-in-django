from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'api/clients', ClientViewSet, basename='api-clients')
router.register(r'api/tasks',   TaskViewSet,   basename='api-tasks')


urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('tasks/', views.task_list, name='task_list'),
]

urlpatterns += [
    path('', include(router.urls)),
]