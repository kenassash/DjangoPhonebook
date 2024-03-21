from django.urls import path
from .views import PhoneHome, PhoneDivision

urlpatterns = [
    path('', PhoneHome.as_view(), name='home'),
    path('<slug:div_slug>/', PhoneDivision.as_view(), name='division'),

]
