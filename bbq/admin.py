from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time_from', 'time_to', 'created_at')
    list_filter = ('date',)
    search_fields = ('user__username',)
