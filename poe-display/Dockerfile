FROM ghcr.io/home-assistant/aarch64-base-python:3.12-alpine3.21

RUN pip install luma.oled pillow
RUN apk add --no-cache freetype-dev libjpeg-turbo-dev zlib-dev ttf-dejavu

COPY display.py /display.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
