# coding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MeterReadingForm
from .models import MeterReading


@login_required
def submit_meter_reading(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST, user=request.user)
        if form.is_valid():
            meter_reading = form.save(commit=False)
            meter_reading.user = request.user
            meter_reading.save()
            return redirect('meters:meter_success')
    else:
        form = MeterReadingForm(user=request.user)
    return render(request, 'meters/submit_reading.html', {'form': form})


@login_required
def user_meter_readings(request):
    user = request.user
    readings = MeterReading.objects.filter(user=user).order_by('-submission_date')
    context = {
        'readings': readings,
        'is_group1': user.group == 'group1',  # Проверка группы
    }
    return render(request, 'meters/user_readings.html', context)
