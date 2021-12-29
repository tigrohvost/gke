FROM python:slim

RUN useradd flaskapi

WORKDIR /home/flaskapi

RUN python -m venv venv
RUN venv/bin/pip install flask
RUN venv/bin/pip install gunicorn

COPY flaskapi.py boot.sh ./

RUN chmod +x boot.sh
ENV FLASK_APP flaskapi.py

RUN chown -R flaskapi:flaskapi ./
USER flaskapi

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
