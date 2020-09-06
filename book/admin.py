from django.contrib import admin
from book.models import BookModel, BodyTextModel, TitleBookBackground, PdfUploadModel
# Register your models here.


class BodyTextModelTabularInline(admin.TabularInline):

    model = BodyTextModel
    extra = 0


@admin.register(BookModel)
class TextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [BodyTextModelTabularInline]

    class Meta:
        model = BookModel


admin.site.register(TitleBookBackground)
admin.site.register(PdfUploadModel)


