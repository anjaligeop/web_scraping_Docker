FROM ubuntu

RUN apt-get update
RUN apt-get install -y python-is-python3 pip
RUN pip install flask

COPY app1.py /opt/
ENTRYPOINT FLASK_APP=/opt/app1.py flask run --host=0.0.0.0

