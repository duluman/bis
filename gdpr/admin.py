from django.contrib import admin
from gdpr.models import RoGdprModel, RoGdprBodyTextModel
from gdpr.models import EnGdprModel, EnGdprBodyTextModel
# Register your models here.


class RoBodyTextModelTabularInline(admin.TabularInline):

    model = RoGdprBodyTextModel
    extra = 0


@admin.register(RoGdprModel)
class RoGdprAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [RoBodyTextModelTabularInline]

    class Meta:
        model = RoGdprModel


class EnBodyTextModelTabularInline(admin.TabularInline):

    model = EnGdprBodyTextModel
    extra = 0


@admin.register(EnGdprModel)
class EnGdprAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [EnBodyTextModelTabularInline]

    class Meta:
        model = EnGdprModel


