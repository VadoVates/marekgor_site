import requests
from webpage import settings


def verify_recaptcha(token):
    """
    Weryfikuj token reCAPTCHA za pomocą serwera Google.

    Args:
        token (str): Token wygenerowany przez reCAPTCHA na stronie klienta.

    Returns:
        dict: Wynik weryfikacji od Google, zawierający klucz 'success' i inne szczegóły.
    """
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': token,
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result