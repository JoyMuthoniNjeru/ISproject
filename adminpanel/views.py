from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TestSlot
from .forms import TestSlotForm

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

