from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .forms import PaymentForm
from .models import Booking, Payment
from adminpanel.models import TestSlot
from testcentre.models import TestCentre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

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
    
    test_centres = TestCentre.objects.all()
    slots_by_centre = TestSlot.objects.all()

    return render(request, 'booking/booking.html', {
        'form': form,
        'test_centres': test_centres,
        'slots': slots_by_centre
    })

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

def is_admin(user):
    return user.userprofile.user_type == 'admin'

@user_passes_test(is_admin)
def confirmed_bookings_view(request):
    bookings = Booking.objects.filter(confirmed=True).select_related('test_slot', 'test_slot__test_centre')
    return render(request, 'adminpanel/confirmed_bookings.html', {'bookings': bookings})
