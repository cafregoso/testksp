FROM python:3.10

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD python manage.py runserver