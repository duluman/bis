from django.shortcuts import render
from shop.forms import BookForm, MultipleBooks
from django.forms import formset_factory
# Create your views here.


def shop_view(request):
    return render(request, 'shop/shop.html')


def order_view(request):
    multiple_form = MultipleBooks()
    if request.method == "POST":
        filled_form = BookForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = "Thanks for your ordering '{}'".format(filled_form.cleaned_data["title"])
            new_form = filled_form

            context = {'form': new_form,
                       'multiple_form': multiple_form,
                       'note': note}

            return render(request, 'shop/order.html', context)

    else:
        form = BookForm()

        context = {'form': form,
                   'multiple_form': multiple_form}

        return render(request, 'shop/order.html', context)


def books_view(request):
    number = 2
    filled_multiple_books = MultipleBooks(request.GET)

    if filled_multiple_books.is_valid():
        number = filled_multiple_books.cleaned_data['number']

    BookFormSet = formset_factory(BookForm, extra=number)

    formset = BookFormSet

    if request.method == 'POST':
        filled_formset = BookFormSet(request.POST)
        if filled_formset.is_valid():
            note = "Books were ordered"
        else:
            note = "Order was not created"

        context = {
            'note': note,
            'formset': formset
        }
        return render(request, 'shop/books.html', context)

    else:
        return render(request, 'shop/books.html', {'formset': formset})
