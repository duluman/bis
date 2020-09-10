
from django.shortcuts import render
from a_home_page.models import HomePageTitleTop, EnHomePageTitleTop


def home_page(request):
    return render(request, "home_page.html")


def read_more(request):
    return render(request, "read_more.html")


def creative_page(request):
    title_list = HomePageTitleTop.objects.all()
    context = {
        "title_list": title_list
    }
    return render(request, "homepage.html", context)


def en_creative_page(request):
    title_list = EnHomePageTitleTop.objects.all()
    context = {
        "title_list": title_list
    }
    return render(request, "en_homepage.html", context)
