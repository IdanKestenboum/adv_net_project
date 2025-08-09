FROM python:3.10-bullseye

RUN apt-get update && \
    apt-get install -y net-tools iputils-ping curl procps && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY slow_post_threads.py .
COPY slowloris.py .

CMD ["/bin/bash"]
