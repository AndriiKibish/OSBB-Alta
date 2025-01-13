# coding: utf-8

from django.db import models
from users.models import User


class MeterReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meter_readings')
    cold_water_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Холодна вода 1')
    cold_water_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Холодна вода 2')
    hot_water_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Гаряча вода 1')
    hot_water_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Гаряча вода 2')
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата подання')

    class Meta:
        verbose_name = "Лічильник"
        verbose_name_plural = "Лічильники"

    def __str__(self):
        return f"Показання від {self.user} ({self.submission_date})"





