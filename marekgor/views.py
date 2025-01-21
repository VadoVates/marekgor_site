from django.shortcuts import render
from django.core.mail import send_mail
from marekgor.forms import ContactForm
from marekgor.utils import verify_recaptcha
from webpage import settings

def index(request):
    return render(request, 'index.html')

def about (request):
    return render (request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Pobierz token reCAPTCHA z formularza
        token = request.POST.get('captcha')
        recaptcha_result = verify_recaptcha(token)
        print(f"reCAPTCHA result: {recaptcha_result}")

        # Walidacja formularza i reCAPTCHA
        if form.is_valid() and recaptcha_result.get('success') and recaptcha_result.get('score', 0) >= 0.8:
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                # Wysyłanie wiadomości e-mail
                send_mail(
                    subject='Formularz kontaktowy',
                    message=f'Nazwa: {name}\nE-mail: {email}\n\n{message}',
                    from_email=email,
                    recipient_list=[settings.RECIPIENT_EMAIL],
                )
                return render(request, 'contact_success.html', {'form': form})
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'contact.html', {
                    'form': form,
                    'error': 'There was an error sending your message. Please try again later.'
                })
        else:
            print(f"Form validation or reCAPTCHA failed: {form.errors}, {recaptcha_result}")
            return render(request, 'contact.html', {
                'form': form,
                'error': 'Invalid form data or failed reCAPTCHA. Please try again.'
            })
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def marek(request):
    return render(request, 'marek.html')