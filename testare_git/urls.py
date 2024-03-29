"""testare_git URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from testare_git.views import home_page, read_more, creative_page, en_creative_page
from django.conf import settings
from django.conf.urls.static import static

# you can change the header am title form de admin page
admin.site.site_header = " Boanca Ionut Silviu Admin Page"
admin.site.site_title = " Admin "


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_view'),
    path('visitromania/', view=home_page),
    path('', view=creative_page, name='home'),
    path('en/', view=en_creative_page, name='en_home'),
    path('read_more/', view=read_more),
    path('hotel/', include("hotel.urls")),
    path('review/', include("review.urls")),
    path('users/', include("users.urls")),
    path('users/activate/', include("activation.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('payments/', include("payments.urls")),
    path('story/', include("story.urls")),
    path('personal-development/', include("personal.urls")),
    path('professional-development/', include("professional.urls")),
    path('gratitude/', include("gratitude.urls")),
    path('direction/', include("direction.urls")),
    path('events/', include("event.urls")),
    path('resources/text/', include("text.urls")),
    path('resources/audio/', include("audio.urls")),
    path('resources/video/', include("video.urls")),
    path('resources/interviews/', include("interview.urls")),
    path('resources/tools/', include("tool.urls")),
    path('resources/books/', include("book.urls")),
    path('search/', include("search.urls")),
    path('linkedin/', include("linkedin.urls")),
    path('shop/', include("shop.urls")),
    path('gdpr/', include("gdpr.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
