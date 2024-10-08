FROM python:3.7-slim

ENV debian_frontend=noninteractive

RUN pip install scapy
RUN apt update && \
    apt install -y libpcap-dev inetutils-ping

COPY scripts/start_snooping.sh /tmp/start_snooping.sh

RUN chmod u+x /tmp/start_snooping.sh
WORKDIR /code
ENTRYPOINT ["/tmp/start_snooping.sh" ]