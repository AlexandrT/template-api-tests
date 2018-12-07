FROM python:3.6

WORKDIR /root

RUN mkdir -p /root/www/playrix

WORKDIR www/playrix

COPY requirements.txt /root/www/playrix/requirements.txt

RUN pip install -r requirements.txt

COPY . /root/www/playrix

CMD ["./docker-entrypoint.sh"]
