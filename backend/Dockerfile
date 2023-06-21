FROM python:3.9-slim

WORKDIR /

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y libgomp1 gcc python3-dev
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

COPY . /app

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
#CMD python app.py 
#the --port(8000) must match with the EXPOSE port above(8000)