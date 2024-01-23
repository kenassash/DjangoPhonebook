from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class PhoneNumber(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя", blank=True)
    surname = models.CharField(max_length=50, verbose_name="фамилия")
    second_name = models.CharField(max_length=20, verbose_name="отчество", blank=True)
    position = models.CharField(max_length=150, verbose_name="должность", blank=True)
    phone = models.CharField(max_length=20, verbose_name="телефон")
    short_phone = models.CharField(max_length=20, verbose_name="короткий №", blank=True)
    cabinet = models.CharField(max_length=20, verbose_name="кабинет", blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="дата и время создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="дата и время обновления")

    is_published = models.BooleanField(default=True, verbose_name="опубликовано")

    division = TreeForeignKey('Division', on_delete=models.PROTECT, null=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, blank=True, editable=False)
    def get_absolute_url(self):
        return reverse('user_data', kwargs={"post_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Телефонны'
        verbose_name_plural = 'Телефонны'
        ordering = ['-create_at']


class Division(MPTTModel):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование организации')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()
    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('division', kwargs={'div_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
