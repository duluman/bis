from django.urls import path
from gdpr.views import ro_gdpr_view, en_gdpr_view

app_name = 'gdpr'

urlpatterns = [
    path('', view=ro_gdpr_view, name='ro_gdpr'),
    path('en/', view=en_gdpr_view, name='en_gdpr')]
