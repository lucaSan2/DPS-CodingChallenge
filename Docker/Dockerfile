FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY sarima.pkl ./
COPY df_train.csv ./

COPY inference.py ./

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "inference:app"]
