FROM ubuntu

MAINTAINER Anjali George P

RUN apt-get update
RUN apt-get install -y python-is-python3 pip
RUN pip install flask
RUN pip install requests
RUN pip install bs4
RUN mkdir -p /opt/templates

COPY app1.py /opt/
COPY templates/* /opt/templates/

ENTRYPOINT FLASK_APP=/opt/app1.py flask run --host=0.0.0.0

