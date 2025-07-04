from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .forms import PaymentForm
from .models import Booking, Payment
from django.contrib.auth.decorators import login_required

@login_required
def make_booking(request):
    if request.user.userprofile.user_type != 'applicant':
        return redirect('/login/')

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect(f'/booking/payment/{booking.id}/')  
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})

def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()

            # Mark booking as confirmed
            booking.confirmed = True
            booking.save()

            return redirect('/booking/payment-success/')
    else:
        form = PaymentForm()

    return render(request, 'booking/payment.html', {
        'form': form,
        'booking': booking,
    })


def payment_success(request):
    return render(request, 'booking/payment_success.html')