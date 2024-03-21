# ������� �������� �������� db � ��������������� � db_test
# ���� ������� � ������� PhoneNumber ������� TEst

import pytest
from django.conf import settings
from phonebook.models import PhoneNumber


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_test.sqlite3',
    }


@pytest.fixture(scope='function')
def django_db_setup_2(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        PhoneNumber.objects.create(surname='TEst')


@pytest.mark.django_db
def test_phone_number_creation():
    # ���������, ��� ������ PhoneNumber ��� ������� ������ � �������� "TEst"
    assert PhoneNumber.objects.filter(surname='TEst').exists()
