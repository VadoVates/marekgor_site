from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from webpage import settings

import logging
logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3(
            attrs={"required_score": 0.8}
        )
    )
    name = forms.CharField(max_length=100, label="Your name:")
    email = forms.EmailField(label="Your email address:")
    message = forms.CharField(widget=forms.Textarea, label="Your message:")

    def clean(self):
        cleaned_data = super().clean()
        logger.info("Captcha validation response: %s", self.cleaned_data.get("captcha"))
        return cleaned_data