FROM openjdk:8

WORKDIR /app

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install antlr4-python3-runtime

RUN curl https://www.antlr.org/download/antlr-4.8-complete.jar -o /root/antlr.jar
ENV ANTLR_JAR=/root/antlr.jar