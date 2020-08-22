from django.shortcuts import render
from story.models import MyStory, StoryBackground

# Create your views here.


def story_view(request):
    story_list = MyStory.objects.all()
    background_list = StoryBackground.objects.all()

    context = {
        'story_list_template': story_list,
        'background_list_template': background_list}

    return render(request, 'story/story.html', context)

