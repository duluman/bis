from django.urls import path
from linkedin.views import cv_view

app_name = 'linkedin'

urlpatterns = [
    path('', view=cv_view, name='cv')]
