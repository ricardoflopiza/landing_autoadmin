from django.contrib import admin
from .models import LandingPageSettings

# Register your models here.
class LandingSettingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(LandingPageSettings,LandingSettingsAdmin)

