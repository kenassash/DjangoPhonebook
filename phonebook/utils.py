from django.db.models import Q

from phonebook.models import *

class SearchMixin:


    def perform_search(self, query):

        phone_numbers = PhoneNumber.objects.filter(
            Q(surname__iregex=query) | Q(name__iregex=query) | Q(second_name__iregex=query),
            is_published=True
        )

        divisions = Division.objects.filter(
            Q(title__iregex=query)
        )



        queryset = list(phone_numbers) + list(divisions)


        return queryset