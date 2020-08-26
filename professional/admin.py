from django.contrib import admin
from professional.models import ProfessionalDevelopment, ProfessionalBackground, BestFeatureCounter
# Register your models here.


class ProfessionalDevelopmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'date')

    class Meta:
        model = ProfessionalDevelopment


# class BestFeatureCounterTabularInline(admin.TabularInline):
#
#     model = BestFeatureCounter
#     extra = 0


admin.site.register(ProfessionalDevelopment, ProfessionalDevelopmentAdmin)
admin.site.register(ProfessionalBackground)
admin.site.register(BestFeatureCounter)

