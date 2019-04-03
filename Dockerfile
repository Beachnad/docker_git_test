FROM python:3.6

WORKDIR /usr/src/app
COPY . .

CMD [ "python", "test_math.py" ]