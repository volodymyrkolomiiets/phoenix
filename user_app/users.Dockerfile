# users.Dockerfile

FROM python:3.9.12
WORKDIR userapp
ENV hello=1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["run.py"]
