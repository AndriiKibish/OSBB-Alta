# coding: utf-8

from django import forms
from .models import MeterReading


class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['cold_water_1', 'cold_water_2', 'hot_water_1', 'hot_water_2']
        widgets = {
            'cold_water_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Показник лічильника холодної води 1'}),
            'cold_water_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Показник лічильника холодної води 2'}),
            'hot_water_1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Показник лічильника гарячої води 1'}),
            'hot_water_2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Показник лічильника гарячої води 2'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Настраиваем отображение полей в зависимости от группы пользователя
        if user and user.group == 'group1':
            self.fields['cold_water_2'].widget = forms.HiddenInput()
            self.fields['hot_water_2'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        cold_water_1 = cleaned_data.get("cold_water_1")
        hot_water_1 = cleaned_data.get("hot_water_1")

        # Проверяем, что обязательные поля заполнены
        if cold_water_1 is None:
            self.add_error('cold_water_1', 'Це поле обов’язкове.')
        if hot_water_1 is None:
            self.add_error('hot_water_1', 'Це поле обов’язкове.')

        return cleaned_data
