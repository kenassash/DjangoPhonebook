from django.db.models import Q
from phonebook.models import PhoneNumber, Division


class SearchMixin:

    def perform_search(self, query):
        phone_numbers = PhoneNumber.objects.filter(
            Q(surname__iregex=query) | Q(name__iregex=query) | Q(second_name__iregex=query),
            is_published=True
        )

        divisions = Division.objects.filter(
            Q(title__iregex=query)
        )

        # Возвращаем результаты телефонных номеров и категорий в виде словаря
        queryset = {
            'phone_numbers': list(phone_numbers),
            'divisions': list(divisions)
        }
        return queryset
