FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/kimmekimme/PycharmProjects.git

WORKDIR /home/PycharmProjects/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-!s=^cd*8$=jykn^khfd%pv-$o=e-rrrf=tqq454i*t2+*d8hww" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0"]
