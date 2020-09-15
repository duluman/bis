from django.shortcuts import render
from gdpr.models import RoGdprModel, EnGdprModel, RoGdprBodyTextModel, EnGdprBodyTextModel
# Create your views here.


def ro_gdpr_view(request):
    text_list = RoGdprModel.objects.all()
    body_list = RoGdprBodyTextModel.objects.all()

    context = {
        'ro_gdpr_list': text_list,
        'body': body_list
        }

    return render(request, 'gdpr/ro_gdpr.html', context)


def en_gdpr_view(request):
    text_list = EnGdprModel.objects.all()
    body_list = EnGdprBodyTextModel.objects.all()

    context = {
        'en_gdpr_list': text_list,
        'body': body_list
        }

    return render(request, 'gdpr/en_gdpr.html', context)
