FROM python:3.6
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN sed -i 's#http://security.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
