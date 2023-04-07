#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

#COPY ./requirements.txt /app/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

FROM python:3.9.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


