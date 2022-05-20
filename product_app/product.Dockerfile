FROM python:3.9.12
WORKDIR productapp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["run.py"]