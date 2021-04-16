from django import forms
from.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'Title',
            'Author',
            'Publisher',
            'Genre',
            'ISBN',
            'Location',
            'Comments'
        ]