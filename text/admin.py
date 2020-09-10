from django.contrib import admin
from text.models import TextModel, BodyTextModel, TextPageBackground, PdfUploadModelForText
from text.models import EnTextModel, EnBodyTextModel, EnTextPageBackground, EnPdfUploadModelForText
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


# English admin


class EnBodyTextModelTabularInline(admin.TabularInline):

    model = EnBodyTextModel
    extra = 0


@admin.register(EnTextModel)
class EnTextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [EnBodyTextModelTabularInline]

    class Meta:
        model = EnTextModel


admin.site.register(EnTextPageBackground)

admin.site.register(EnPdfUploadModelForText)
