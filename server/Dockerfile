FROM python:3.7-stretch

ADD . /server

WORKDIR /

RUN python -m venv /env

RUN /env/bin/pip install --upgrade pip
RUN /env/bin/pip install --no-cache-dir -r /server/requirements.txt

WORKDIR /server

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

CMD gunicorn app:"create_app()" --bind=server:8000 --reload
