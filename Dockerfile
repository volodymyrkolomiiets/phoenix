# Dockerfile

FROM python:3.9.12
WORKDIR userapp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /userapp
ENTRYPOINT ["python"]
CMD ["run.py"]
