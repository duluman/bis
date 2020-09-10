from django.shortcuts import render
from audio.models import AudioModel, AudioTitleTop, AudioModelSound
from audio.models import EnAudioModel, EnAudioTitleTop, EnAudioModelSound

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


# english


def en_audio_view(request):
    audio_list = EnAudioModel.objects.all()
    background_list = EnAudioTitleTop.objects.all()
    sounds = EnAudioModelSound.objects.all()
    context = {
        'song': audio_list,
        'background_list_template': background_list,
        'sounds': sounds}

    return render(request, 'audio/en_audio_list.html', context)


def en_audio_single_view(request, enaudiomodel_id):
    audio_single = EnAudioModel.objects.filter(id=enaudiomodel_id)
    background_list = EnAudioTitleTop.objects.all()
    sounds = EnAudioModelSound.objects.all()
    context = {
        'song': audio_single,
        'background_list_template': background_list,
        'sounds': sounds
    }

    return render(request, 'audio/en_audio_single.html', context)
