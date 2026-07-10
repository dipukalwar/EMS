from django.contrib import admin
from django.utils import timezone
from .models import Event,Bookings,ExpiredEvent

class EventAdmin(admin.ModelAdmin):
    list_display=["name","seats","dnt"]


admin.site.register(Event,EventAdmin)
admin.site.register(Bookings)

class ExpiredEventAdmin(admin.ModelAdmin):
    def get_queryset(self,request):
        return super().get_queryset(request).filter(dnt__lt=timezone.now())
    
admin.site.register(ExpiredEvent,ExpiredEventAdmin)