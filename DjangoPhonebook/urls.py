from django.contrib import admin
from django.urls import path, include

from phonebook.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phonebook.urls')),
]
