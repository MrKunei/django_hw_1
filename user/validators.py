from django.db.models import Func, F
from django.db.models.functions import ExtractYear
from rest_framework import serializers


class DomainValidator():
    def __init__(self, mail):
        if not isinstance(mail, list):
            mail = [mail]

        self.mail = mail

    def __call__(self, value):
        values = value.split('@')
        if values[1] in self.mail:
            raise serializers.ValidationError('Домен недоступен!')


class BirthDayValidator():
    def __call__(self, date):
        age = ExtractYear(Func(F('date'), function='age'))
        if age < 9:
            raise serializers.ValidationError('Вы младше 9 лет!')
