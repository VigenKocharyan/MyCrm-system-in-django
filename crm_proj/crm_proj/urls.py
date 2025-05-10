# crm_proj/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Класс-разлогинщик, допускающий GET-запросы
class LogoutGetView(LogoutView):
    http_method_names = ['get', 'post']
    next_page = 'login'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='client_list', permanent=False)),
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls')),

    # Auth
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='crm/login.html'),
         name='login'),
    path('accounts/logout/',
         LogoutGetView.as_view(),
         name='logout'),
]
