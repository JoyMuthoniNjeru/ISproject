from django.shortcuts import render, redirect, get_object_or_404
from .models import TestCentre
from .forms import TestCentreForm
from django.contrib.auth.decorators import login_required

@login_required
def manage_test_centres(request):
    if request.user.userprofile.user_type != 'manager':
        return redirect('/login/')
    
    centres = TestCentre.objects.filter(manager=request.user)

    if request.method == 'POST':
        form = TestCentreForm(request.POST)
        if form.is_valid():
            new_centre = form.save(commit=False)
            new_centre.manager = request.user
            new_centre.save()
            return redirect('/testcentre/manage/')
    else:
        form = TestCentreForm()

    return render(request, 'testcentre/manage.html', {
        'form': form,
        'centres': centres
    })

@login_required
def delete_test_centre(request, pk):
    centre = get_object_or_404(TestCentre, pk=pk, manager=request.user)
    centre.delete()
    return redirect('/testcentre/manage/')

@login_required
def edit_test_centre(request, pk):
    centre = get_object_or_404(TestCentre, pk=pk, manager=request.user)

    if request.method == 'POST':
        form = TestCentreForm(request.POST, instance=centre)
        if form.is_valid():
            form.save()
            return redirect('/testcentre/manage/')
    else:
        form = TestCentreForm(instance=centre)

    return render(request, 'testcentre/edit.html', {
        'form': form,
        'centre': centre
    })


