FROM debian

RUN apt update && \
    apt install -y curl iproute2 net-tools

COPY scripts/host.sh /tmp/host.sh
RUN chmod u+x /tmp/host.sh

ENTRYPOINT [ "/tmp/host.sh" ]