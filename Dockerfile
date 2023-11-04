FROM python:3.10-alpine

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . .

RUN mkdir data
RUN cd src/
CMD python main.py