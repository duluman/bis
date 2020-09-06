from django.contrib import admin
from direction.models import Direction, DirectionTitleTop, BestFeatureCounter, BestFeatureCounterTitle
# Register your models here.


class DirectionAdmin(admin.ModelAdmin):

    list_display = ['title']

    class Meta:
        model = Direction

        
class DirectionTitleTopAdmin(admin.ModelAdmin):

    list_display = ['title', 'subtitle']

    class Meta:
        model = DirectionTitleTop


admin.site.register(Direction, DirectionAdmin)
admin.site.register(DirectionTitleTop, DirectionTitleTopAdmin)
admin.site.register(BestFeatureCounter)
admin.site.register(BestFeatureCounterTitle)
