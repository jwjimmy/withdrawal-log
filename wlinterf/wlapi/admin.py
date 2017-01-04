from django.contrib import admin
from wlapi.models import Visit

class VisitAdmin(admin.ModelAdmin):
	list_display = ('visited_at', 'reason')

# Register your models here.

admin.site.register(Visit, VisitAdmin)