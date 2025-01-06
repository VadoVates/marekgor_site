import requests
from webpage import settings


def verify_recaptcha(token):
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': token,
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result
