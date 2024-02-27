from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm, QualityCheckForm
from .models import Vehicle, QualityCheck

@login_required
def vehicle_info(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            # Logic to retrieve vendor and product information based on P.O. number
            # Not implemented in this example
            vehicle.save()
            return redirect('quality_check', vehicle_id=vehicle.id)
    else:
        form = VehicleForm()
    return render(request, 'vehicle/vehicle_info.html', {'form': form})

@login_required
def quality_check(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method == 'POST':
        form = QualityCheckForm(request.POST)
        if form.is_valid():
            quality_check = form.save(commit=False)
            quality_check.vehicle = vehicle
            quality_check.save()
            vehicle.quality_check_passed = quality_check.passed
            vehicle.save()
            return redirect('checkout', vehicle_id=vehicle.id)
    else:
        form = QualityCheckForm()
    return render(request, 'vehicle/quality_check.html', {'form': form, 'vehicle': vehicle})

# Other views for authentication, checkout, etc...
