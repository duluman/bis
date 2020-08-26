from django.shortcuts import render
from professional.models import ProfessionalDevelopment, ProfessionalBackground, BestFeatureCounter

# Create your views here.


def professional_view(request):
    professional_list = ProfessionalDevelopment.objects.all()
    background_list = ProfessionalBackground.objects.all()
    counter = BestFeatureCounter.objects.all()

    context = {
        'professional_list_template': professional_list,
        'background_list_template': background_list,
        'feature_list': counter}

    return render(request, 'professional/professional_development.html', context)
