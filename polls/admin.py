from django.contrib import admin
from .models import *

class InfoAdmin(admin.ModelAdmin):
    """Model for display event infomation in admin page."""
    list_display = (
        'first_name',
        'gender',
    )

admin.site.register(Info,InfoAdmin)
