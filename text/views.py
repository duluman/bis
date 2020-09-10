from django.shortcuts import render
from text.models import TextModel, BodyTextModel, TextPageBackground, PdfUploadModelForText
from text.models import EnTextModel, EnBodyTextModel, EnTextPageBackground, EnPdfUploadModelForText

# Create your views here.


def text_view(request):
    text_list = TextModel.objects.all()
    background_list = TextPageBackground.objects.all()
    pdf_text = PdfUploadModelForText.objects.all()

    context = {
        'text_list_template': text_list,
        'background_list_template': background_list,
        'pdf_text': pdf_text}

    return render(request, 'text/text.html', context)


def details(request, textmodel_id):
    text_list = TextModel.objects.filter(id=textmodel_id)
    post_text = BodyTextModel.objects.filter(heading_id=textmodel_id)
    background_list = TextModel.objects.filter(id=textmodel_id)

    context = {
        "post_text_details": post_text,
        'background_list_template': background_list,
        'text_list_template': text_list,
    }

    return render(request, "text/details.html", context)


def details_pdf_text(request, id):
    pdf_text = PdfUploadModelForText.objects.filter(id=id)

    context = {
        "pdf_text": pdf_text}

    return render(request, "text/pdf_details_text.html", context)


# for the english version


def en_text_view(request):
    text_list = EnTextModel.objects.all()
    background_list = EnTextPageBackground.objects.all()
    pdf_text = EnPdfUploadModelForText.objects.all()

    context = {
        'text_list_template': text_list,
        'background_list_template': background_list,
        'pdf_text': pdf_text}

    return render(request, 'text/en_text.html', context)


def en_details(request, entextmodel_id):
    text_list = EnTextModel.objects.filter(id=entextmodel_id)
    post_text = EnBodyTextModel.objects.filter(heading_id=entextmodel_id)
    background_list = EnTextModel.objects.filter(id=entextmodel_id)

    context = {
        "post_text_details": post_text,
        'background_list_template': background_list,
        'text_list_template': text_list,
    }

    return render(request, "text/en_details.html", context)


def en_details_pdf_text(request, id):
    pdf_text = EnPdfUploadModelForText.objects.filter(id=id)

    context = {
        "pdf_text": pdf_text}

    return render(request, "text/en_pdf_details_text.html", context)


# am eliminat background pentru pagina de detalii
# {% for element in background_list_template %}
#
# {% if element.picture %}
#   <div class="view jarallax" data-jarallax='{"speed": 0.01}' style="background-image: url('{{ MEDIA_URL }}{{ element.picture }}'); background-repeat: no-repeat; background-size: cover; background-position: center center;">
#     <!-- Mask & flexbox options-->
#     <div class="mask rgba-white-light d-flex justify-content-center align-items-center">
#       <!-- Content -->
#       <div class="container">
#         <!--Grid row-->
#         <div class="row">
#           <!--Grid column-->
#           <div class="col-md-12 black-text text-center">
#             <h1 class="display-4 mb-0 pt-md-5 pt-5 black-text font-weight-bold wow fadeInDown" data-wow-delay="3s">{{ element.title }}
#
#             </h1>
#             <h5 class="text-uppercase pt-md-5 pt-sm-2 pt-5 pb-md-5 pb-sm-3 pb-5 black-text font-weight-bold wow fadeInDown"
#               data-wow-delay="2s">{{ element.subtitle }}</h5>
#
#           </div>
#           <!--Grid column-->
#         </div>
#         <!--Grid row-->
#       </div>
#       <!-- Content -->
#     </div>
#     <!-- Mask & flexbox options-->
#   </div>
#
# {% endif %}
# {% endfor %}
# {% if not  element in background_list_template %}
# <br><br><br>
# {% endif %}