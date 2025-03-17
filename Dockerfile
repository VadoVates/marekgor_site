# Obraz bazowy z Pythona
FROM python:3.11-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik zależności jako osobną warstwę (optymalizacja)
COPY requirements.txt .

# Instalujemy zależności przed skopiowaniem reszty kodu (lepsze cache'owanie)
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy całą aplikację
COPY . .

# Otwieramy port aplikacji (jeśli trzeba)
EXPOSE 8001

# Uruchamiamy Gunicorna jako WSGI serwer
CMD ["gunicorn", "-b", "0.0.0.0:8001", "webpage.wsgi:application"]
