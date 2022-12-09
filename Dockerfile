FROM python:3.8.3
WORKDIR /kantinitbtst
COPY requirements.txt /kantinitbtst/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /kantinitbtst
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080","--reload"]