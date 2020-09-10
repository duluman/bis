from django.contrib import admin
from book.models import BookModel, BodyTextModel, TitleBookBackground, PdfUploadModel
from book.models import EnBookModel, EnBodyTextModel, EnTitleBookBackground, EnPdfUploadModel
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


# english


class EnBodyTextModelTabularInline(admin.TabularInline):

    model = EnBodyTextModel
    extra = 0


@admin.register(EnBookModel)
class EnTextAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    inlines = [EnBodyTextModelTabularInline]

    class Meta:
        model = EnBookModel


admin.site.register(EnTitleBookBackground)
admin.site.register(EnPdfUploadModel)
