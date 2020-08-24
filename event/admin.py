from django.contrib import admin
from event.models import EventModel, EventBackground
# Register your models here.




class EventAdmin(admin.ModelAdmin):

    list_display = ['title']

    class Meta:
        model = EventModel


admin.site.register(EventModel, EventAdmin)
admin.site.register(EventBackground)
