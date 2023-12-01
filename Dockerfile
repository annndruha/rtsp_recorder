FROM python:3.11.1

COPY ./requirements.txt /app/
RUN apt-get update && apt-get install libgl1 -y
RUN pip install -U --no-cache-dir -r /app/requirements.txt

COPY ./src /app/src

WORKDIR /app

CMD ["python", "-m", "src"]