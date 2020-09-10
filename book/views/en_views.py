from django.shortcuts import render
from book.models import EnBookModel, EnBodyTextModel, EnTitleBookBackground, EnPdfUploadModel

# Create your views here.


def en_book_view(request):
    text_list = EnBookModel.objects.all()
    body_list = EnBodyTextModel.objects.all()
    background_list = EnTitleBookBackground.objects.all()
    pdf_list = EnPdfUploadModel.objects.all()
    context = {
        'book_list_template': text_list,
        'body_list_template': body_list,
        'background_list_template': background_list,
        'pdf_list': pdf_list
    }

    return render(request, 'book/en_book.html', context)


def en_details(request, enbookmodel_id):
    post_text = EnBodyTextModel.objects.filter(heading_id=enbookmodel_id)
    book = EnBookModel.objects.filter(id=enbookmodel_id)

    context = {
        "post_text_details": post_text,
        "book_show": book
    }

    return render(request, "book/en_details.html", context)


def en_details_pdf(request, id):
    pdf_book = EnPdfUploadModel.objects.filter(id=id)

    context = {
        "pdf_book": pdf_book
    }

    return render(request, "book/en_pdf_details.html", context)
