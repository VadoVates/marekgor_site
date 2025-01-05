from django.shortcuts import render
from django.core.mail import send_mail
from marekgor.forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about (request):
    return render (request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def marek(request):
    # mareks = Marek.objects.all()
    return render(request, 'marek.html')