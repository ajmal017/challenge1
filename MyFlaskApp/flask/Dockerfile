FROM python:3-onbuild

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
ADD . /app

RUN pip install -r requirements.txt

CMD ["python","run.py" ] 