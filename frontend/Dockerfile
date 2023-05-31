FROM python:3.9-slim

WORKDIR /app
ADD . /app

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y libgomp1 gcc python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app


#CMD streamlit run --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false script.py
#CMD ["python", "script.py"]

ENTRYPOINT ["streamlit", "run", "script.py", "--server.port=8501", "--server.address=0.0.0.0"]