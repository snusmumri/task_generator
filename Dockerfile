FROM python:3.8


#RUN pip3 install flask requests
#RUN apt-get install -y python3-flask python3-requests
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "task_api.py"]