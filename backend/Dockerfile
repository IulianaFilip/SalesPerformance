#
FROM python:3.9


#
WORKDIR /user/src/backend/app
# WORKDIR /user/src/backend/app # TODO: switch to this one
#

COPY ./requirements.txt requirements.txt
#


RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
# 

EXPOSE 8000:8000
# 

COPY . .


#

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]