FROM python:3.6.8-slim-stretch

COPY . /

RUN pip install -r requirements.txt && \
    pip install -e .[test]

EXPOSE 5002
