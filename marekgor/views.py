from django.shortcuts import render
from django.core.mail import send_mail
from marekgor.forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about (request):
    return render (request, 'about.html')

from marekgor.utils import verify_recaptcha

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        token = request.POST.get('g-recaptcha-response')
        recaptcha_result = verify_recaptcha(token)
        print(f"reCAPTCHA result: {recaptcha_result}")

        if form.is_valid() and recaptcha_result.get('success'):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject='Formularz kontaktowy',
                    message=f'Nazwa: {name}\nE-mail: {email}\n\n{message}',
                    from_email=email,
                    recipient_list=['contact@marekgor.com'],
                )
                return render(request, 'contact_success.html', {'form': form})
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print(f"Form validation failed: {form.errors}")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def marek(request):
    # mareks = Marek.objects.all()
    return render(request, 'marek.html')