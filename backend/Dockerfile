FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
#CMD python app.py 
#the --port(8000) must match with the EXPOSE port above(8000)