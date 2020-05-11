FROM python:3.6-alpine
RUN apk add --update python py-pip
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
    build-base \
    mariadb-dev ;\
    pip install mysqlclient;\
    apk del .build-deps 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY run.py run.py

CMD python run.py

