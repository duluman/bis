from django.contrib import admin
from tool.models import ToolModel, BodyTextModel, ToolPageBackground
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
