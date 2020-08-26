from django.shortcuts import render
from book.models import BookModel, BodyTextModel

# Create your views here.


def book_view(request):
    text_list = BookModel.objects.all()
    body_list = BodyTextModel.objects.all()

    context = {
        'book_list_template': text_list,
        'body_list_template': body_list}

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

