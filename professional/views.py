from django.shortcuts import render
from professional.models import ProfessionalDevelopment, ProfessionalBackground, BestFeatureCounter, BestFeatureCounterTitle, RoProfessionalCounterPicture
from professional.models import EnProfessionalDevelopment, EnProfessionalBackground, EnBestFeatureCounter, EnBestFeatureCounterTitle, EnProfessionalCounterPicture

# Create your views here.


def professional_view(request):
    professional_list = ProfessionalDevelopment.objects.all()
    background_list = ProfessionalBackground.objects.all()
    counter = BestFeatureCounter.objects.all()
    title_list = BestFeatureCounterTitle.objects.all()
    counter_picture = RoProfessionalCounterPicture.objects.all()
    context = {
        'professional_list_template': professional_list,
        'background_list_template': background_list,
        'feature_list': counter,
        'title_list': title_list,
        'counter_picture': counter_picture}

    return render(request, 'professional/professional_development.html', context)


def en_professional_view(request):
    professional_list = EnProfessionalDevelopment.objects.all()
    background_list = EnProfessionalBackground.objects.all()
    counter = EnBestFeatureCounter.objects.all()
    title_list = EnBestFeatureCounterTitle.objects.all()
    counter_picture = EnProfessionalCounterPicture.objects.all()

    context = {
        'professional_list_template': professional_list,
        'background_list_template': background_list,
        'feature_list': counter,
        'title_list': title_list,
        'counter_picture': counter_picture}

    return render(request, 'professional/en_professional_development.html', context)
