from django.shortcuts import render
from story.models import MyStory, StoryBackground, EnMyStory, EnStoryBackground

# Create your views here.


def story_view(request):
    story_list = MyStory.objects.all()
    background_list = StoryBackground.objects.all()

    context = {
        'story_list_template': story_list,
        'background_list_template': background_list}

    return render(request, 'story/story.html', context)


def en_story_view(request):
    story_list = EnMyStory.objects.all()
    background_list = EnStoryBackground.objects.all()

    context = {
        'story_list_template': story_list,
        'background_list_template': background_list}

    return render(request, 'story/en_story.html', context)

