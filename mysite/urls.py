from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('notebooks/<str:notebook_name>/', views.view_notebook, name='view_notebook'),
]
