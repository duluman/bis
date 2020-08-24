from django.shortcuts import render, get_object_or_404
from text.models import TextModel, BodyTextModel, TextPageBackground

# Create your views here.


def text_view(request):
    text_list = TextModel.objects.all()
    background_list = TextPageBackground.objects.all()

    context = {
        'text_list_template': text_list,
        'background_list_template': background_list}

    return render(request, 'text/text.html', context)


def details(request, textmodel_id):
    post_text = BodyTextModel.objects.filter(heading_id=textmodel_id)
    background_list = TextModel.objects.filter(id=textmodel_id)

    context = {
        "post_text_details": post_text,
        # "heading_id": textmodel_id,
        'background_list_template': background_list
    }

    return render(request, "text/details.html", context)

