from django.contrib import admin
from event.models import EventModel, EventBackground
from event.models import EnEventModel, EnEventBackground
# Register your models here.


class EventAdmin(admin.ModelAdmin):

    list_display = ['title']

    class Meta:
        model = EventModel


admin.site.register(EventModel, EventAdmin)
admin.site.register(EventBackground)


class EnEventAdmin(admin.ModelAdmin):

    list_display = ['title']

    class Meta:
        model = EnEventModel


admin.site.register(EnEventModel, EnEventAdmin)
admin.site.register(EnEventBackground)
