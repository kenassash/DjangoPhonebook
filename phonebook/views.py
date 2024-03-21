from django.conf.urls import handler404
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from .models import *
from .utils import *


class PhoneHome(SearchMixin, ListView):
    model = PhoneNumber
    template_name = 'phonebook/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Телефонный справочник'}

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.perform_search(query)


class PhoneDivision(SearchMixin, ListView):
    model = Division
    template_name = 'phonebook/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Телефонный справочник'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['children_divisions'] = Division.objects.get(slug=self.kwargs['div_slug']).get_children()

        return context

    def get_queryset(self):
        phone_numbers = PhoneNumber.objects.filter(division__slug=self.kwargs['div_slug'], is_published=True)
        # divisions = Division.objects.filter(slug=self.kwargs['div_slug'])

        # Комбинирование результатов в один список
        queryset = {
            'phone_numbers': list(phone_numbers)
            # 'divisions': list(divisions)
        }
        return queryset

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except (Http404, Division.DoesNotExist):
            return handler404(request, None, template_name='phonebook/index.html')
