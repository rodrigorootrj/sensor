FROM python:3.10
RUN mkdir /app/ /asset/
COPY /asset/requirements.txt /asset/
WORKDIR /app/
RUN pip install -r /asset/requirements.txt