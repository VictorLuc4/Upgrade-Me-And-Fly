FROM python:3

COPY . /app
COPY ./requirements.txt /app

EXPOSE 5000

RUN pip3 install -r /app/requirements.txt

CMD python3 /app/upgradeMe.py


