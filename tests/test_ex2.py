# -*- coding: cp1251 -*-

import pytest
from phonebook.models import PhoneNumber


@pytest.fixture
def myfixture(django_db_blocker):
    with django_db_blocker.unblock():
        # Проверяем, существует ли запись "Мавлеткулов" в базе данных
        return PhoneNumber.objects.filter(surname='Мавлеткулов').exists()


def test_myfixture(myfixture):
    assert myfixture
