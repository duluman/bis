from django.shortcuts import render
from book.models import EnBookModel, EnBodyTextModel as EnBookTextModel
from django.db.models import Q
from story.models import EnMyStory
from personal.models import EnPersonalDevelopment
from professional.models import EnProfessionalDevelopment
from gratitude.models import EnGratitudeAndThankfulness
# from review.models import AppReview
from direction.models import EnDirection
from event.models import EnEventModel
from text.models import EnTextModel, EnBodyTextModel
from audio.models import EnAudioModel
from video.models import EnVideoModel
from interview.models import EnInterviewModel
from tool.models import EnBodyTextModel as EnToolBodyModel
# Create your views here.


def en_search_view(request):
    search_term = ''

    try:
        search_term = request.POST['search_for']
        book_list = EnBookModel.objects.filter(Q(title__icontains=search_term) | Q(subtitle__icontains=search_term))
        book_body_list = EnBookTextModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        story_list = EnMyStory.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        personal_list = EnPersonalDevelopment.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        professional_list = EnProfessionalDevelopment.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        gratitude_list = EnGratitudeAndThankfulness.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        # review_list = AppReview.objects.filter(Q(profession__icontains=search_term) | Q(comment__icontains=search_term))
        direction_list = EnDirection.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        event_list = EnEventModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        text_list = EnTextModel.objects.filter(Q(title__icontains=search_term) | Q(subtitle__icontains=search_term))
        body_text_list = EnBodyTextModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        audio_list = EnAudioModel.objects.filter(
            Q(title__icontains=search_term) |
            Q(author__icontains=search_term) |
            Q(category__icontains=search_term) |
            Q(body__icontains=search_term)
        )
        video_list = EnVideoModel.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term))
        interview_list = EnInterviewModel.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term))
        tool_list = EnToolBodyModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))

    except Exception as e:
        book_list = EnBookModel.objects.all()
        book_body_list = EnBookTextModel.objects.all()
        story_list = EnMyStory.objects.all()
        personal_list = EnPersonalDevelopment.objects.all()
        professional_list = EnProfessionalDevelopment.objects.all()
        gratitude_list = EnGratitudeAndThankfulness.objects.all()
        # review_list = AppReview.objects.all()
        direction_list = EnDirection.objects.all()
        event_list = EnEventModel.objects.all()
        text_list = EnTextModel.objects.all()
        body_text_list = EnBodyTextModel.objects.all()
        audio_list =EnAudioModel.objects.all()
        video_list = EnVideoModel.objects.all()
        interview_list = EnInterviewModel.objects.all()
        tool_list = EnToolBodyModel.objects.all()

    context = {
        'search_term': search_term,
        'book_list': book_list,
        'book_body_list': book_body_list,
        'story_list': story_list,
        'personal_list': personal_list,
        'professional_list': professional_list,
        'gratitude_list': gratitude_list,
        # 'review_list': review_list,
        'direction_list': direction_list,
        'event_list': event_list,
        'text_list': text_list,
        'body_text_list': body_text_list,
        'audio_list': audio_list,
        'video_list': video_list,
        'interview_list': interview_list,
        'tool_list': tool_list,

    }

    return render(request, "search/en_search.html", context)

