FROM python:3.7.3-slim

WORKDIR ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod 644 app.py

CMD [ "python", "./app.py" ]