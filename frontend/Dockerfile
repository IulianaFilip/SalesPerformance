FROM python:3.9

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 5000

CMD streamlit run --server.port 8051 --server.enableCORS false overview.py

