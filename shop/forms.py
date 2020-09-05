from django import forms
from shop.models import BookModel

# class BookForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100)
#     author = forms.CharField(label='Author', max_length=100)
#     type = forms.ChoiceField(label='Type', choices=[('Pdf','Pdf'),('Word','Word')])


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'type']
        labels = {'title': 'Titlu', 'author': 'Autor'}
        widgets = {'title': forms.Textarea}


class MultipleBooks(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
