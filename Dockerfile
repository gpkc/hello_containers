FROM python:3.6.4-slim

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app

ENV HOME /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "hello_containers.py" ]
