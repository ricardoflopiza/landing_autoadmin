# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LandingPageSettings
from .forms import LandingPageSettingsForm



# @login_required
def edit_landing_page(request):
    settings = LandingPageSettings.objects.last()
    if request.method == 'POST':
        form = LandingPageSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = LandingPageSettingsForm(instance=settings)
    return render(request, 'edit_landing_page.html', {'form': form})

def landing_page(request):
    settings = LandingPageSettings.objects.last()
    return render(request, 'landing_page.html', {'settings': settings})
