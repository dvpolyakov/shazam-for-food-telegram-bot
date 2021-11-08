FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir /app/

COPY ./service/tgbot/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

#RUN wget -q -O braces_demo_photos.tar.gz https://www.dropbox.com/s/l7p1exrl8ymsagh/braces_demo_photos.tar.gz?dl=0
#RUN tar -xzvf braces_demo_photos.tar.gz

#RUN ["chmod", "+x", "./service/tgbot/setup_clickhouse_orm.sh"]
#RUN ./service/tgbot/setup_clickhouse_orm.sh

ENV PRJPATH /app/
CMD ["python", "-um", "service.tgbot.code.run"]