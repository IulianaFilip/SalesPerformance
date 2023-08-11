FROM python:3.9

WORKDIR /user/src/frontend

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501

CMD streamlit run --server.port 8501 --server.enableCORS false overview.py

