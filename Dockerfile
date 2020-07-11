FROM python:3

COPY . /app
COPY ./requirements.txt /app

ENV PORT 8080

EXPOSE $PORT

RUN apt update 
RUN apt install python-pip -y
RUN pip2 install Pillow

RUN pip3 install -r /app/requirements.txt

CMD python3 /app/upgradeMe.py


