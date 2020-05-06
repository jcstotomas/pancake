FROM python:3.6-alpine
RUN apk add --update python py-pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY run.py run.py

CMD python run.py

