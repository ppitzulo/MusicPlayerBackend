FROM python:3.11.6

ENV PYTHONUNBUFFERED=1

ENV DEMO_MODE=False

RUN addgroup --system django && adduser --system --group django

WORKDIR /music_player

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R django:django /music_player

USER django

# Generate a Django secret key and store it in an environment variable
RUN SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(50))") && \
    echo "DJANGO_SECRET_KEY=$SECRET_KEY" > .env

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
