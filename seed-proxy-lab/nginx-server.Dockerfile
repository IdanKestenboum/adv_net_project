FROM nginx:1.25-bullseye

RUN apt-get update && \
    apt-get install -y procps net-tools iputils-ping curl && \
    rm -rf /var/lib/apt/lists/*
