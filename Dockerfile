FROM python:3.12
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    pip install psycopg2-binary
COPY . /app
RUN ls
ENTRYPOINT ["python", "serve.py"]
