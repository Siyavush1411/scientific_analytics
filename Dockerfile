FROM python:3.12

WORKDIR /scientific_analytics

COPY . .

RUN apt-get update && apt-get install -y python3-distutils
RUN pip install poetry
RUN poetry install

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
