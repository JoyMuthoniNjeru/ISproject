from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from booking.models import Booking, TestSlot
from .forms import TestSlotForm
from django.contrib.auth.decorators import user_passes_test

@login_required
def admin_dashboard(request):
    if request.user.userprofile.user_type != 'admin':
        return redirect('/login/')

    slots = TestSlot.objects.all().order_by('-date')

    if request.method == 'POST':
        form = TestSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/adminpanel/dashboard/')
    else:
        form = TestSlotForm()

    return render(request, 'adminpanel/dashboard.html', {
        'form': form,
        'slots': slots,
    })

@login_required
def delete_slot(request, pk):
    slot = get_object_or_404(TestSlot, pk=pk)
    slot.delete()
    return redirect('/adminpanel/dashboard/')

@login_required
def edit_slot(request, pk):
    slot = get_object_or_404(TestSlot, pk=pk)

    if request.method == 'POST':
        form = TestSlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('/adminpanel/dashboard/')
    else:
        form = TestSlotForm(instance=slot)

    return render(request, 'adminpanel/edit_slot.html', {'form': form, 'slot': slot})

def is_admin(user):
    return user.userprofile.user_type == 'admin'

@user_passes_test(is_admin)
def confirmed_bookings_view(request):
    bookings = Booking.objects.filter(confirmed=True).select_related('test_slot', 'test_slot__test_centre')
    return render(request, 'adminpanel/confirmed_bookings.html', {'bookings': bookings})


@user_passes_test(is_admin)
def slot_config_view(request):
    from testcentre.models import TestCentre

    selected_centre_id = request.GET.get('centre')
    selected_date = request.GET.get('date')

    if selected_centre_id:
        slots = TestSlot.objects.filter(test_centre_id=selected_centre_id).select_related('test_centre')
    else:
        slots = TestSlot.objects.all().select_related('test_centre')

    if selected_date:
        slots = slots.filter(date=selected_date)


    if request.method == 'POST':
        form = TestSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('slot_config')
    else:
        form = TestSlotForm()

    centres = TestCentre.objects.all()

    return render(request, 'adminpanel/dashboard.html', {
        'slots': slots,
        'form': form,
        'centres': centres,
        'selected_centre_id': selected_centre_id,
        'selected_date': selected_date,
    })