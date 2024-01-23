from django.conf.urls import handler404
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


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
    extra_context = {'title': 'Телефонный справочник'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['posts']:
            context['div_selected'] = context['posts'][0].division_id
        else:
            context['div_selected'] = None

        division = Division.objects.get(slug=self.kwargs['div_slug'])
        context['division'] = division
        context['children_divisions'] = division.get_children()
        return context


    def get_queryset(self):
        return PhoneNumber.objects.filter(division__slug=self.kwargs['div_slug'], is_published=True)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return handler404(request, None, template_name='phonebook/index.html')


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




