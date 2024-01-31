from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import *


class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'surname',
        'name',
        'second_name',
        'position',
        'phone',
        'short_phone',
        'cabinet',
        'is_published',
        'division',

    )

    list_display_links = (
        'surname',
        'name',
        'second_name',

    )
    search_fields = (
        'surname',
        'name',
        'second_name',
    )

    list_editable = ('is_published',)


class DivisionAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(PhoneNumber, PhoneAdmin)
admin.site.register(Division, DivisionAdmin)

