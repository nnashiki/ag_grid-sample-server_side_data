FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
