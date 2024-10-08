FROM python:3.7-slim

WORKDIR /app

COPY scripts/server.py /app/server.py
COPY scripts/swen_crypto.py /app/swen_crypto.py
COPY scripts/start_server.sh /tmp/start_server.sh

RUN pip install Flask cryptography
RUN mkdir /app/output && touch /app/output/passwords.txt

RUN chmod u+x /tmp/start_server.sh
ENTRYPOINT [ "/tmp/start_server.sh" ]