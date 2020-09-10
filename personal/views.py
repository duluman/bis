from django.shortcuts import render
from personal.models import PersonalDevelopment, PersonalBackground, EnPersonalDevelopment, EnPersonalBackground

# Create your views here.


def personal_view(request):
    personal_list = PersonalDevelopment.objects.all()
    background_list = PersonalBackground.objects.all()

    context = {
        'personal_list_template': personal_list,
        'background_list_template': background_list}

    return render(request, 'personal/personal_development.html', context)


def en_personal_view(request):
    personal_list = EnPersonalDevelopment.objects.all()
    background_list = EnPersonalBackground.objects.all()

    context = {
        'personal_list_template': personal_list,
        'background_list_template': background_list}

    return render(request, 'personal/en_personal_development.html', context)
