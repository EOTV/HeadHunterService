FROM python:3.12-bullseye

RUN mkdir data_transfer

WORKDIR /hh_parsing

COPY . .

RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN cd src/

ENTRYPOINT [ "bash" ]