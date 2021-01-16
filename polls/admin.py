from django.contrib import admin
from .models import *

class InfoAdmin(admin.ModelAdmin):
    """Model for display event infomation in admin page."""
    list_display = (
        'first_name',
        'gender',
    )
class EducationAdmin(admin.ModelAdmin):
    """Model for display user infomation in admin page."""
    list_display = (
        'university',
    )

admin.site.register(Info,InfoAdmin)
admin.site.register(Education, EducationAdmin)
