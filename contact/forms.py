from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=500)
    email = forms.EmailField(required=True, max_length=500)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=5000)
