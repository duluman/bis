from django.urls import path
from review.views import app_review_view, AddReviewView, en_app_review_view, EnAddReviewView


app_name = 'review'

urlpatterns = [
    path('', view=app_review_view, name='app_review'),
    path('add', AddReviewView.as_view(), name='add_review'),
    path('en/', view=en_app_review_view, name='en_app_review'),
    path('en/add', EnAddReviewView.as_view(), name='en_add_review')
]

