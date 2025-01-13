# coding: utf-8

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(AbstractUser):
    GROUP_CHOICES = [
        ('group1', 'Група 1 (по одному лічильнику на холодну і гарячу воду)'),
        ('group2', 'Група 2 (по два лічильники на холодну і гарячу воду)'),
    ]
    group = models.CharField(
        max_length=10,
        choices=GROUP_CHOICES,
        default='group1',
        verbose_name='Група'
    )
    username = models.PositiveIntegerField(
        unique=True,
        validators=[
            MinValueValidator(1, "Номер квартири не може бути меншим за 1."),
            MaxValueValidator(120, "Номер квартири не може бути більше 120.")
        ],
        verbose_name="Номер квартири"
    )
    email = models.EmailField(unique=True, verbose_name="Електронна пошта")
    first_name = None
    last_name = None

    def __str__(self):
        return f"{self.username} - {self.get_group_display()}"




