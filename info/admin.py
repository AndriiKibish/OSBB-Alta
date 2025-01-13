from django.contrib import admin
from .models import Contact, News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'short_content')
    ordering = ('-publication_date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment')
    search_fields = ('name', 'phone')
