from django_recaptcha import fields
from django import forms
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    captcha = fields.ReCaptchaField(widget=ReCaptchaV3(required_score=0.8, action="submit"))
    name = forms.CharField(max_length=100, label="Your name:")
    email = forms.EmailField(label="Your email address:")
    message = forms.CharField(widget=forms.Textarea, label="Your message:")