from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
import os

# Create your views here.


def contact(request):
    form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def submit(request):
    print("test in submit")
    form = ContactForm(data=request.POST)
    if form.is_valid():
        subject = "Message from portfolio website"
        body = {
            "email": form.cleaned_data["email"],
            "name": form.cleaned_data["name"],
            "message": form.cleaned_data["message"],
        }
        message = "\n".join(body.values())

    try:
        send_mail(
            subject, message, os.getenv("EMAIL_RECIEVER"), [os.getenv("EMAIL_RECIEVER")]
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return render(request, "contact/thanks.html")
