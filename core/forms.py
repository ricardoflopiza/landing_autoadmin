
# forms.py
from django import forms
from .models import LandingPageSettings

class LandingPageSettingsForm(forms.ModelForm):
    class Meta:
        model = LandingPageSettings
        fields = ['title', 'subtitle', 'description', 'background_color', 'text_color']
