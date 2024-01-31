# Generated by Django 5.0.1 on 2024-01-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='cabinet',
            field=models.CharField(blank=True, max_length=150, verbose_name='кабинет'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='name',
            field=models.CharField(blank=True, max_length=150, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(max_length=150, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='second_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='отчество'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='surname',
            field=models.CharField(max_length=150, verbose_name='фамилия'),
        ),
    ]
