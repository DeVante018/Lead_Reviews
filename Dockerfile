FROM python:3.9.1

ENV HOME /root
WORKDIR /root
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=localhost
COPY . .
RUN pip install -r requirements.txt && \
    pip install flask_login && \
    pip install flask_pymongo && \
    pip install flask-socketio

EXPOSE 80

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

CMD ["python3", "server.py"]
