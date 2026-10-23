from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "book_fullname",
            "book_email",
            "book_date",
            "book_guests",
            "book_message",
        ]
        labels = {
            "book_fullname": "Full Name",
            "book_email": "Email",
            "book_date": "Date",
            "book_guests": "Number of guests",
            "book_message": "Special Requests",
        }
        widgets = {
            "book_fullname":forms.TextInput(attrs={"class":"form-control"}),
            "book_email":forms.EmailInput(attrs={"class":"form-control"}),
            "book_date":forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            "book_guests":forms.NumberInput(attrs={"class":"form-control"}),
            "book_message":forms.Textarea(attrs={"class":"form-control"}),
        }
