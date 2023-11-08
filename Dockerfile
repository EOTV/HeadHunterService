FROM python:3.10-bullseye
 
ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.33.0
ENV FIREFOX_VER 87.0
 
RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
       firefox-esr \
   && pip install  \
       requests \
       selenium
 
# Add latest FireFox
RUN set -x \
   && apt install -y \
       libx11-xcb1 \
       libdbus-glib-1-2 \
   && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
   && tar -jxf firefox-* \
   && mv firefox /opt/ \
   && chmod 755 /opt/firefox \
   && chmod 755 /opt/firefox/firefox
  
# Add geckodriver
RUN set -x \
   && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/

RUN mkdir hh_parsing
COPY . ./hh_parsing

RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install -r ./hh_parsing/requirements.txt

RUN apt-get update \
    && apt-get install -y tar \
    && tar xvzf geckodriver-v0.33.0-linux64.tar.gz \
    && tar xvjf firefox-87.0.tar.bz2 \
    && mv geckodriver hh_parsing/src/repositories/

WORKDIR /hh_parsing/src

CMD ["python", "main.py"]