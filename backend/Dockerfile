FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install flask boto3
COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]