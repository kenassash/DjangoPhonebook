from django.contrib import admin
from django.urls import path, include
from DjangoPhonebook import settings

from phonebook.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phonebook.urls')),
    # path("__debug__/", include("debug_toolbar.urls")),
]
