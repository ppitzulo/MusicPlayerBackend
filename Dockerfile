FROM python:3.11.6

ENV PYTHONUNBUFFERED=1

RUN addgroup --system django && adduser --system --group django

WORKDIR /music_player

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R django:django /music_player

USER django

# Generate a Django secret key for demo and dev and store it in an environment variable
RUN DJANGO_SECRET_KEY_DEMO=$(python -c "import secrets; print(secrets.token_urlsafe(50))") && \
    echo "DJANGO_SECRET_KEY_DEMO=$DJANGO_SECRET_KEY_DEMO" > .env

RUN DJANGO_SECRET_KEY_DEV=$(python -c "import secrets; print(secrets.token_urlsafe(50))") && \
    echo "DJANGO_SECRET_KEY_DEV=$DJANGO_SECRET_KEY_DEV" >> .env


EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
