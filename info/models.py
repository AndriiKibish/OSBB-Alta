# coding: utf-8

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    publication_date = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    content = models.TextField(verbose_name="Новина")

    def __str__(self):
        return self.title

    def short_content(self):
        return self.content[:100] + "..." if len(self.content) > 100 else self.content

    class Meta:
        verbose_name = "Новина"
        verbose_name_plural = "Новини"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    phone = models.CharField(max_length=20, verbose_name="Номер телефону")
    comment = models.TextField(blank=True, verbose_name="Додаткова інформація")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"
