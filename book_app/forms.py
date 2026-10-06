from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
            attrs={"type": "date", "format": "%Y-%m-%d"}
        )
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "author",
            "genre",
            "published_date",
        ]

    def clean_title(self):
        cleaned_title = self.cleaned_data.get("title")
        proper_title = cleaned_title.title()  # Remove leading and trailing whitespace
        # check if the title already exists in the database
        if Book.objects.filter(title=proper_title).exists():
            raise forms.ValidationError("This title already exists in the database, please choose a different title.")

        return proper_title

class UpdateBookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
            attrs={"type": "date", "format": "%Y-%m-%d"}
        )
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "isbn",
            "author",
            "genre",
            "published_date",
        ]
