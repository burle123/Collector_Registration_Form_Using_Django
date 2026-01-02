from django.shortcuts import render, redirect
from .forms import CollectorForm
from django.contrib import messages
from .models import Collector


def collector_registration(request):
    if request.method == "POST":
        form = CollectorForm(request.POST, request.FILES)

        if form.is_valid():
            collector = form.save()
            return redirect('collector_success')

        # Debug
        print(form.errors)

    else:
        form = CollectorForm()

    return render(request, 'collector/registration.html', {"form": form})


def collector_success(request):
    return render(request, 'collector/success.html')


def collector_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        try:
            collector = Collector.objects.filter(
                email=email,
                phone_number=phone_number
            ).first()

            if collector:
                # Store collector ID in session
                request.session['collector_id'] = collector.id
                messages.success(request, "Login successful!")
                return redirect('collector_dashboard')
            else:
                messages.error(request, "Invalid credentials. Please try again.")

        except Collector.DoesNotExist:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'collector/login.html')


def collector_dashboard(request):
    collector_id = request.session.get('collector_id')
    if not collector_id:
        return redirect('collector_login')

    collector = Collector.objects.get(id=collector_id)
    return render(request, 'collector/dashboard.html', {'collector': collector})


def collector_logout(request):
    request.session.flush()
    return redirect('collector_login')
