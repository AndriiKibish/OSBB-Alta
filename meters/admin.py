# coding: utf-8

from django.contrib import admin
from django.http import HttpResponse
from .models import MeterReading
import xlwt


def export_to_xls(modeladmin, request, queryset):
    # Создаём объект Workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Meter Readings')

    # Устанавливаем заголовки
    columns = [
        'Квартира',
        'Дата подачи',
        'Холодна вода 1',
        'Холодна вода 2',
        'Гаряча вода 1',
        'Гаряча вода 2',
    ]

    for col_num, column_title in enumerate(columns):
        worksheet.write(0, col_num, column_title, xlwt.easyxf('font: bold on;'))

    # Добавляем строки из выбранных записей
    for row_num, meter_reading in enumerate(queryset, start=1):
        row_data = [
            meter_reading.user.username,  # Квартира
            meter_reading.submission_date.strftime('%Y-%m-%d'),  # Дата подачи
            meter_reading.cold_water_1,
            meter_reading.cold_water_2 if meter_reading.cold_water_2 is not None else 'N/A',
            meter_reading.hot_water_1,
            meter_reading.hot_water_2 if meter_reading.hot_water_2 is not None else 'N/A',
        ]
        for col_num, cell_value in enumerate(row_data):
            worksheet.write(row_num, col_num, cell_value)

    # Создаём HTTP-ответ с Excel-файлом
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="meter_readings.xls"'
    workbook.save(response)
    return response


@admin.register(MeterReading)
class MeterReadingAdmin(admin.ModelAdmin):
    list_display = ('user', 'cold_water_1', 'cold_water_2', 'hot_water_1', 'hot_water_2', 'submission_date')
    list_filter = ('submission_date', 'user')
    search_fields = ('user__username',)
    ordering = ('-submission_date',)

    actions = [export_to_xls]

    def get_readonly_fields(self, request, obj=None):
        """Делаем дату только для чтения."""
        if obj:  # Редактирование существующей записи
            return self.readonly_fields + ('submission_date',)
        return self.readonly_fields
