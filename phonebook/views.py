from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


menu = [
    {'title': "Добавить телефон", 'url_name': 'addphone'},
    {'title': "Войти", 'url_name': 'login'},
]

class PhoneHome(ListView):
    model = PhoneNumber
    template_name = 'phonebook/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Телефонный справочник'}

    def get_queryset(self):
        return PhoneNumber.objects.filter(is_published=True)


# def index(requests):
#     posts = PhoneNumber.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'div_selected': 0,
#     }
#     return render(requests, 'phonebook/index.html', context=context)

class PhoneDivision(ListView):
    model = PhoneNumber
    template_name = 'phonebook/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return PhoneNumber.objects.filter(division__id=self.kwargs['div_id'], is_published=True)

# def show_division(requests, div_id):
#     posts = PhoneNumber.objects.filter(division=div_id)
#
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Телефонный справочник',
#     }
#     return render(requests, 'phonebook/index.html', context=context)

def addphone(requests):
    return render(requests, 'phonebook/about.html', {'menu': menu, 'title': 'Добавить телефон'})

def login(requests):
    return HttpResponse("Авторизация")



