from django.contrib import admin
from django.urls import path, re_path, include
from todolist import views
from django.conf.urls import url
from todolist import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
]
