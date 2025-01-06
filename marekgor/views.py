from django.shortcuts import render
from django.core.mail import send_mail
from marekgor.forms import ContactForm
import requests
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def about (request):
    return render (request, 'about.html')

def verify_recaptcha(token):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': token
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result.get('success', False)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        recaptcha_token = request.POST.get('g-recaptcha-response')
        recaptcha_valid = verify_recaptcha(recaptcha_token)

        if form.is_valid() and recaptcha_valid:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject='Formularz kontaktowy',
                message=f'Nazwa: {name}\nE-mail: {email}\n\n{message}',
                from_email=email,
                recipient_list=['contact@marekgor.com'],
            )
            return render(request, 'contact_success.html', {'form': form})
        else:
            if not recaptcha_valid:
                form.add_error('captcha', 'Error verifying reCAPTCHA, please try again.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def marek(request):
    # mareks = Marek.objects.all()
    return render(request, 'marek.html')