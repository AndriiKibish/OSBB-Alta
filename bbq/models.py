# coding: utf-8

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Квартира")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Квартира")
    date = models.DateField(verbose_name="Дата")
    time_from = models.TimeField(verbose_name="Час початку")
    time_to = models.TimeField(verbose_name="Час завершення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"
        ordering = ['-date', 'time_from']

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time_from}–{self.time_to}"

    def clean(self):
        # Проверка пересечения времени
        overlapping = Booking.objects.filter(
            date=self.date,
            time_from__lt=self.time_to,
            time_to__gt=self.time_from,
        ).exclude(id=self.id)
        if overlapping.exists():
            raise ValidationError("Цей час вже заброньований.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
