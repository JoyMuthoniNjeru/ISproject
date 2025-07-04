from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def make_booking(request):
    if request.user.userprofile.user_type != 'applicant':
        return redirect('/login/')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect(f'/payment/{booking.id}/')  
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})

