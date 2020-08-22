from django.contrib import admin
from professional.models import ProfessionalDevelopment, ProfessionalBackground
# Register your models here.


class ProfessionalDevelopmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'date')

    class Meta:
        model = ProfessionalDevelopment


admin.site.register(ProfessionalDevelopment, ProfessionalDevelopmentAdmin)
admin.site.register(ProfessionalBackground)
