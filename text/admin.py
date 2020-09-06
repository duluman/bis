from django.contrib import admin
from text.models import TextModel, BodyTextModel, TextPageBackground, PdfUploadModelForText
# Register your models here.


class BodyTextModelTabularInline(admin.TabularInline):

    model = BodyTextModel
    extra = 0


@admin.register(TextModel)
class TextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [BodyTextModelTabularInline]

    class Meta:
        model = TextModel


admin.site.register(TextPageBackground)

admin.site.register(PdfUploadModelForText)
