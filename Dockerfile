FROM python:3.6.4-slim

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

ENV HOME /app

EXPOSE 5000
ENV FLASK_APP app.py
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
