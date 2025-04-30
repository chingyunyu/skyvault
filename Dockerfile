FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/ app/
COPY manage.py .
COPY db/ db/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]