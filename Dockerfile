FROM python:3.11.1-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /mvfp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80