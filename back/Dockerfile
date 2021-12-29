FROM python:slim

RUN useradd back

WORKDIR /home/back

RUN python -m venv venv
RUN venv/bin/pip install flask
RUN venv/bin/pip install gunicorn

COPY back.py boot.sh ./

RUN chmod +x boot.sh
ENV FLASK_APP back.py

RUN chown -R back:back ./
USER back

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
