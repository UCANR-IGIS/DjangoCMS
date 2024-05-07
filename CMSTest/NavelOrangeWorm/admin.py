from django.contrib import admin
from NavelOrangeWorm.models import Event, eventLink

# Register your models here.
class EventInline(admin.StackedInline):
    model = eventLink
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]

admin.site.register(Event,EventAdmin)
