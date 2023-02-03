FROM python:3.11.1-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /mvfp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]