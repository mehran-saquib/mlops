FROM python:3.10.6-slim

WORKDIR /app1

COPY . /app1

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api:app","reload"]




