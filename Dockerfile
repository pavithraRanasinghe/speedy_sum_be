FROM python:3.10

WORKDIR /usr/src/app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]