from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        # fields = ("name", "subject", "email", "message")
        fields = "__all__"


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        # fields = ("name", "subject", "email", "message")
        fields = "__all__"
