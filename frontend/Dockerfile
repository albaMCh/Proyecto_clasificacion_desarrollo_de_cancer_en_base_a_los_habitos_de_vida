FROM python:3.9-slim

WORKDIR /app
ADD . /app

COPY requirements.txt ./requirements.txt
#COPY cancer_patient_data_sets.xlsx ./cancer_patient_data_sets.xlsx

RUN apt-get update && apt-get install -y libgomp1 gcc python3-dev python3-openpyxl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install pandas --upgrade

EXPOSE 8501

COPY . /app


#CMD streamlit run --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false script.py
#CMD ["python", "script.py"]

ENTRYPOINT ["streamlit", "run", "script.py", "--server.port=8501", "--server.address=0.0.0.0"]