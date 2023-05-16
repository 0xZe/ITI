# DockerFile to build containers hosts to test ansible on them 

FROM ubuntu:latest

RUN apt update -y && apt install ssh -y && apt install sudo -y 

RUN adduser ansible

RUN echo "ansible:123" | chpasswd 

RUN usermod -aG sudo ansible

ENTRYPOINT service ssh restart && bash

172.17.0.2