# coding: utf-8

import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bbq:success_bbq')
    else:
        form = BookingForm()
    return render(request, 'bbq/create_booking.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bbq/my_bookings.html', {'bookings': bookings})


@login_required
def all_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bbq/all_bookings.html', {'bookings': bookings})


@login_required
def future_bookings(request):
    today = datetime.date.today()
    bookings = Booking.objects.filter(date__gt=today).order_by('date', 'time_from')
    return render(request, 'bbq/future_bookings.html', {'bookings': bookings})


@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('bbq:my_bookings')
    return render(request, 'bbq/delete_booking.html', {'booking': booking})
