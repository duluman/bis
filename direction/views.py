from django.shortcuts import render
from direction.models import Direction, DirectionTitleTop

# Create your views here.


def direction_view(request):
    direction_list = Direction.objects.all()
    background_list = DirectionTitleTop.objects.all()

    context = {
        'direction_list_template': direction_list,
        'background_list_template': background_list}

    return render(request, 'direction/direction.html', context)

