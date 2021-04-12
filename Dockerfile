FROM python:3.9.1

ENV HOME /root
WORKDIR /root

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "server.py"]