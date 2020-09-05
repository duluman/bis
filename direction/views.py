from django.shortcuts import render
from direction.models import Direction, DirectionTitleTop, BestFeatureCounterTitle, BestFeatureCounter

# Create your views here.


def direction_view(request):
    direction_list = Direction.objects.all()
    background_list = DirectionTitleTop.objects.all()
    counter = BestFeatureCounter.objects.all()
    title_list = BestFeatureCounterTitle.objects.all()

    context = {
        'direction_list_template': direction_list,
        'background_list_template': background_list,
        'feature_list': counter,
        'title_list': title_list}

    return render(request, 'direction/direction.html', context)

