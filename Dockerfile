FROM python:3.7-slim
WORKDIR /usr/src/app
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./
CMD [ "python3", "/usr/src/app/bot-yggtorrent.py" ]