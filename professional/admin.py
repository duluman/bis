from django.contrib import admin
from professional.models import ProfessionalDevelopment, ProfessionalBackground, BestFeatureCounter, BestFeatureCounterTitle
from professional.models import EnProfessionalDevelopment, EnProfessionalBackground, EnBestFeatureCounter, EnBestFeatureCounterTitle
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
admin.site.register(BestFeatureCounterTitle)


class EnProfessionalDevelopmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'date')

    class Meta:
        model = EnProfessionalDevelopment


admin.site.register(EnProfessionalDevelopment, EnProfessionalDevelopmentAdmin)
admin.site.register(EnProfessionalBackground)
admin.site.register(EnBestFeatureCounter)
admin.site.register(EnBestFeatureCounterTitle)
