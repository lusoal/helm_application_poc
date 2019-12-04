FROM python:3.7-slim
ADD requirements.txt /requirements.txt
RUN pip install -r  /requirements.txt
COPY . /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["helm_application_poc.py"]



