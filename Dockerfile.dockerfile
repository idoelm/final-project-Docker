FROM python:3.11-slim

WORKDIR /app

COPY assigment_1.py /app/
COPY config.json /app/
COPY requirements.txt /app/
COPY printColors.py /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python" , "assigment_1.py" ]