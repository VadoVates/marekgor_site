import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
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

#def marek(request):
#    return render(request, 'marek.html')

def calc(request):
    return render(request, 'calc.html')

# Constants
GALLERY_DIR = os.path.join(settings.BASE_DIR, 'static', 'img', 'gallery')
THUMBNAIL_DIR = os.path.join(settings.BASE_DIR, 'static', 'img', 'thumbnails')

def get_exif_data(filepath):
    try:
        image = Image.open(filepath)
        exif_data = image._getexif()
        if not exif_data:
            return None
        gps_data = {}
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
        return gps_data
    except Exception:
        return None

def gps_to_decimal(coord, ref):
    degrees, minutes, seconds = coord
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps(gps_data):
    try:
        lat = gps_data.get('GPSLatitude')
        lat_ref = gps_data.get('GPSLatitudeRef')
        lon = gps_data.get('GPSLongitude')
        lon_ref = gps_data.get('GPSLongitudeRef')
        if lat and lat_ref and lon and lon_ref:
            lat_decimal = gps_to_decimal(lat, lat_ref)
            lon_decimal = gps_to_decimal(lon, lon_ref)
            return lat_decimal, lon_decimal
    except Exception:
        pass
    return None, None

def process_image(filename):
    """
    Processes a single image file: extracts GPS data and prepares image metadata.
    """
    image_path = os.path.join(GALLERY_DIR, filename)
    gps_data = get_exif_data(image_path)
    latitude, longitude = extract_gps(gps_data) if gps_data else (None, None)
    return {
        'original': f'img/gallery/{filename}',
        'thumbnail': f'img/thumbnails/{filename}',
        'latitude': latitude,
        'longitude': longitude,
    }


def gallery(request):
    """
    View to handle gallery page creation.
    Iterates over images and processes for rendering metadata.
    """
    images = [
        process_image(filename)
        for filename in os.listdir(GALLERY_DIR)
        if filename.endswith('.webp') or filename.endswith('.jpg')
    ]
    return render(request, 'gallery.html', {'images': images})
