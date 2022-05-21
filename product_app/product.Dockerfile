FROM python:3.9-alpine
WORKDIR product_app
COPY requirements.txt requirements.txt
ENV PYTHONUNBUFFERED=1
RUN apk add build-base
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["run.py"]