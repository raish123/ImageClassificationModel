FROM python:3.9-slim-buster 
WORKDIR /data
COPY . /data
RUN pip install -r requirements.txt
RUN apt-get update -y && apt-get install awscli -y
CMD ["python","app.py"]