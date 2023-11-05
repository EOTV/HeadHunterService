FROM python:3.10-alpine

WORKDIR /hh_parsing

RUN pip install --upgrade pip

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

RUN cd src/

ENTRYPOINT ["bash"]