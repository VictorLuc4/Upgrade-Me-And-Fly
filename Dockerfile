FROM python:3

COPY . /app
COPY ./requirements.txt /app

ENV PORT 8080

EXPOSE $PORT

RUN pip3 install -r /app/requirements.txt

CMD python3 /app/upgradeMe.py


