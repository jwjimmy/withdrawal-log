from django.contrib import admin
from wlapi.models import Visit, Hit

class VisitAdmin(admin.ModelAdmin):
	list_display = ('visited_at', 'reason')

class HitAdmin(admin.ModelAdmin):
	list_display = ('visited_at',)

# Register your models here.

admin.site.register(Visit, VisitAdmin)
admin.site.register(Hit, HitAdmin)