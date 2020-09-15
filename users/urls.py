from django.urls import path
from users.views import (register, profile, en_profile,
                         handle_login,
                         handle_logout,
                         profile_email,
                         contact_view,
                         en_contact_view,
                         change_password,
                         en_change_password,
                         ro_news_letter,
                         en_news_letter,
                         )


app_name = 'users'

urlpatterns = [

    path('register/', view=register, name='register'),
    path('ro/newsletter/', view=ro_news_letter, name='ro_newsletter'),
    path('en/newsletter/', view=en_news_letter, name='en_newsletter'),
    path('login/', view=handle_login, name='login'),
    path('logout/', view=handle_logout, name='logout'),
    path('contact/', view=contact_view, name='contact'),
    path('en/contact/', view=en_contact_view, name='en_contact'),
    path('profile/', view=profile, name='profile'),
    path('en/profile/', view=en_profile, name='en_profile'),
    path('profile/email', view=profile_email, name='profile_email'),
    path('change_password/', view=change_password, name='change_password'),
    path('en/change_password/', view=en_change_password, name='en_change_password'),
    ]


