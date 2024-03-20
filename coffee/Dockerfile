
FROM python:alpine

WORKDIR /app

COPY coffee.py .
COPY grain.py .

RUN pip install pymongo

CMD ["python", "seeder.py"]
