FROM python:3.7.6-buster
RUN mkdir /app
RUN mkdir /mnt/data
ADD . /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FILE_PATH=/mnt/data/ip_log.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]