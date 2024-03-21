# -*- coding: cp1251 -*-

# Этот тест проверяет создание объекта модели PhoneNumber с заданными атрибутами.

import pytest
from phonebook.models import PhoneNumber, Division


@pytest.fixture
def division():
    di = Division.objects.create(title='Test Division', slug='test-division')
    return di


@pytest.fixture
def phone_number(division):
    phone_number = PhoneNumber.objects.create(
        surname='TestSurname',
        name='TestName',
        second_name='TestSecondName',
        position='TestPosition',
        phone='123456789',
        short_phone='123',
        cabinet='TestCabinet',
        division=division
    )
    return phone_number


@pytest.mark.django_db
def test_phone_number_creation(phone_number):
    assert phone_number.surname == 'TestSurname'
    assert phone_number.name == 'TestName'
    assert phone_number.second_name == 'TestSecondName'
    assert phone_number.position == 'TestPosition'
    assert phone_number.phone == '123456789'
    assert phone_number.short_phone == '123'
    assert phone_number.cabinet == 'TestCabinet'
    assert phone_number.division.title == 'Test Division'
