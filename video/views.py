from django.shortcuts import render
from video.models import VideoModel, VideoTitleTop
from video.models import EnVideoModel, EnVideoTitleTop

# Create your views here.


def video_view(request):
    video_list = VideoModel.objects.all()
    background_list = VideoTitleTop.objects.all()

    context = {
        'video_list_template': video_list,
        'background_list_template': background_list}

    return render(request, 'video/video.html', context)


def en_video_view(request):
    video_list = EnVideoModel.objects.all()
    background_list = EnVideoTitleTop.objects.all()

    context = {
        'video_list_template': video_list,
        'background_list_template': background_list}

    return render(request, 'video/en_video.html', context)
