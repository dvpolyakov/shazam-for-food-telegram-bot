FROM pytorch/pytorch:latest
RUN apt-get update -y
RUN apt-get install -y python-pip
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN mkdir /app/
RUN mkdir /app/weights

COPY ./service/image_handler/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app/
ENV PRJPATH /app/
CMD ["python", "-um", "service.image_handler.run"]