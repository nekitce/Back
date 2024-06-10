"""
URL configuration for Kaluta_DZ2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import corsheaders
from Furniture_App.views import parts_by_furniture_id, part_info, delete_furniture, show_furniture_info, \
    create_furniture, update_furniture

urlpatterns = [
    path("admin/", admin.site.urls),
    path('furniture/', show_furniture_info, name='show_furniture_info'),
    path('furniture/<int:furniture_id>/parts/', parts_by_furniture_id, name='parts_by_furniture_id'),
    path('part/<int:part_id>/', part_info, name='part_info'),
    path('furniture/delete/<int:furniture_id>/', delete_furniture, name='delete_furniture'),
    path('create_furniture/', create_furniture, name='create_furniture'),
    path('update_furniture/', update_furniture, name='update_furniture')
]
