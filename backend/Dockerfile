#
FROM python:3.9


#
WORKDIR /code
#

COPY ./requirements.txt /app/requirements.txt
#


RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
# 

EXPOSE 8000:8000
# 

COPY . /app/code/app


#

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]