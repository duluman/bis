from django.shortcuts import render
from book.models import BookModel, BodyTextModel as BookTextModel
from django.db.models import Q
from story.models import MyStory
from personal.models import PersonalDevelopment
from professional.models import ProfessionalDevelopment
from gratitude.models import GratitudeAndThankfulness
from review.models import AppReview
from direction.models import Direction
from event.models import EventModel
from text.models import TextModel, BodyTextModel
from audio.models import AudioModel
from video.models import VideoModel
from interview.models import InterviewModel
from tool.models import BodyTextModel as ToolBodyModel
# Create your views here.


def search_view(request):
    search_term = ''

    try:
        search_term = request.POST['search_for']
        book_list = BookModel.objects.filter(Q(title__icontains=search_term) | Q(subtitle__icontains=search_term))
        book_body_list = BookTextModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        story_list = MyStory.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        personal_list = PersonalDevelopment.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        professional_list = ProfessionalDevelopment.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        gratitude_list = GratitudeAndThankfulness.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        review_list = AppReview.objects.filter(Q(profession__icontains=search_term) | Q(comment__icontains=search_term))
        direction_list = Direction.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        event_list = EventModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        text_list = TextModel.objects.filter(Q(title__icontains=search_term) | Q(subtitle__icontains=search_term))
        body_text_list = BodyTextModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))
        audio_list = AudioModel.objects.filter(
            Q(title__icontains=search_term) |
            Q(author__icontains=search_term) |
            Q(category__icontains=search_term) |
            Q(body__icontains=search_term)
        )
        video_list = VideoModel.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term))
        interview_list = InterviewModel.objects.filter(Q(title__icontains=search_term) | Q(category__icontains=search_term))
        tool_list = ToolBodyModel.objects.filter(Q(title__icontains=search_term) | Q(body__icontains=search_term))

    except Exception as e:
        book_list = BookModel.objects.all()
        book_body_list = BookTextModel.objects.all()
        story_list = MyStory.objects.all()
        personal_list = PersonalDevelopment.objects.all()
        professional_list = ProfessionalDevelopment.objects.all()
        gratitude_list = GratitudeAndThankfulness.objects.all()
        review_list = AppReview.objects.all()
        direction_list = Direction.objects.all()
        event_list = EventModel.objects.all()
        text_list = TextModel.objects.all()
        body_text_list = BodyTextModel.objects.all()
        audio_list = AudioModel.objects.all()
        video_list = VideoModel.objects.all()
        interview_list = InterviewModel.objects.all()
        tool_list = ToolBodyModel.objects.all()

    context = {
        'search_term': search_term,
        'book_list': book_list,
        'book_body_list': book_body_list,
        'story_list': story_list,
        'personal_list': personal_list,
        'professional_list': professional_list,
        'gratitude_list': gratitude_list,
        'review_list': review_list,
        'direction_list': direction_list,
        'event_list': event_list,
        'text_list': text_list,
        'body_text_list': body_text_list,
        'audio_list': audio_list,
        'video_list': video_list,
        'interview_list': interview_list,
        'tool_list': tool_list,

    }

    return render(request, "search/search.html", context)


    # {% for item in text_list %}
    #     <div class="col-md-6">
    #         <h4> {{ item.title }}</h4>
    #         <p class="text-justify">{{ item.subtitle }}</p>
    #          <p>Cuvantul cheie cautat apare pe pagina <a href="{% url 'text:text' %}">"Text" </a> la titlul {{ item.title }}</p>
    #     <hr></div>
    # {% endfor %}