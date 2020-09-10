from django.shortcuts import render
from book.models import BookModel, BodyTextModel, TitleBookBackground, PdfUploadModel

# Create your views here.


def book_view(request):
    text_list = BookModel.objects.all()
    body_list = BodyTextModel.objects.all()
    background_list = TitleBookBackground.objects.all()
    pdf_list = PdfUploadModel.objects.all()
    context = {
        'book_list_template': text_list,
        'body_list_template': body_list,
        'background_list_template': background_list,
        'pdf_list': pdf_list
    }

    return render(request, 'book/book.html', context)


def details(request, bookmodel_id):
    post_text = BodyTextModel.objects.filter(heading_id=bookmodel_id)
    book = BookModel.objects.filter(id=bookmodel_id)
    # print(book.title)
    # print(book.subtitle)
    # print(book.image)
    print(book)

    context = {
        "post_text_details": post_text,
        "book_show": book}

    return render(request, "book/details.html", context)


def details_pdf(request, id):
    pdf_book = PdfUploadModel.objects.filter(id=id)

    context = {
        "pdf_book": pdf_book}

    return render(request, "book/pdf_details.html", context)
