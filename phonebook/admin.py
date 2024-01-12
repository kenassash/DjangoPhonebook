from django.contrib import admin

from .models import *


class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'surname',
        'second_name',
        'position',
        'phone',
        'short_phone',
        'cabinet',
        'is_published',
        'division',

    )

    list_display_links = (
        'id',
        'name',
    )
    search_fields = (
        'name',
        'surname',
    )

    list_editable = ('is_published',)

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(PhoneNumber, PhoneAdmin)
admin.site.register(Division, DivisionAdmin)

