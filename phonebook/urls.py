from django.urls import path

from .views import *

urlpatterns = [
    path('', PhoneHome.as_view(), name='home'),
    path('addphone/', addphone, name='addphone'),
    path('login/', login, name='login'),

    path('div/<int:div_id>/', PhoneDivision.as_view(), name='division'),
]
