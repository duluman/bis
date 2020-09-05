from django.shortcuts import render
from audio.models import AudioModel, AudioTitleTop, AudioModelSound

# Create your views here.


def audio_view(request):
    audio_list = AudioModel.objects.all()
    background_list = AudioTitleTop.objects.all()
    sounds = AudioModelSound.objects.all()
    context = {
        'song': audio_list,
        'background_list_template': background_list,
        'sounds': sounds}

    return render(request, 'audio/audio_list.html', context)


def audio_single_view(request, audiomodel_id):
    audio_single = AudioModel.objects.filter(id=audiomodel_id)
    background_list = AudioTitleTop.objects.all()
    sounds = AudioModelSound.objects.all()
    context = {
        'song': audio_single,
        'background_list_template': background_list,
        'sounds': sounds
    }

    return render(request, 'audio/audio_single.html', context)
