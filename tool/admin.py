from django.contrib import admin
from tool.models import ToolModel, BodyTextModel, ToolPageBackground
from tool.models import EnToolModel, EnBodyTextModel, EnToolPageBackground
# Register your models here.


class BodyTextModelTabularInline(admin.TabularInline):

    model = BodyTextModel
    extra = 0


@admin.register(ToolModel)
class TextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [BodyTextModelTabularInline]

    class Meta:
        model = ToolModel


admin.site.register(ToolPageBackground)


# english


class EnBodyTextModelTabularInline(admin.TabularInline):

    model = EnBodyTextModel
    extra = 0


@admin.register(EnToolModel)
class EnTextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [EnBodyTextModelTabularInline]

    class Meta:
        model = EnToolModel


admin.site.register(EnToolPageBackground)
