FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN mkdir /app/


COPY ./service/image_uploader/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/

ENV PRJPATH /app/
CMD ["python", "-um", "service.image_uploader.run"]