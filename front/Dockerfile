FROM python:slim

RUN useradd front

WORKDIR /home/front

RUN python -m venv venv
RUN venv/bin/pip install flask
RUN venv/bin/pip install requests
RUN venv/bin/pip install gunicorn

COPY front.py boot.sh ./

RUN chmod +x boot.sh
ENV FLASK_APP front.py

RUN chown -R front:front ./
USER front

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
