FROM python:3.11.6

ENV PYTHONUNBUFFERED=1

# RUN addgroup --system django && adduser --system --group django

WORKDIR /music_player

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R 1000:1000 /music_player
#
# USER django

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
