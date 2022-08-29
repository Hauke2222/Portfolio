from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


def contact(request):
    form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})


def submit(request):
    print("test in submit")
    form = ContactForm(data=request.POST)
    if form.is_valid():
        subject = "Website Inquiry"
        body = {
            "name": form.cleaned_data["name"],
            "email": form.cleaned_data["email"],
            "message": form.cleaned_data["message"],
        }
        message = "\n".join(body.values())

    try:
        send_mail(subject, message, "admin@example.com", ["admin@example.com"])
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return HttpResponse("Bedankt voor uw bericht.")
