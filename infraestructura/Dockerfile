FROM python:3.7.7-alpine3.11
RUN pip install flask
RUN pip install flask_restful
RUN pip install mysql-connector
RUN pip install python-dateutil
RUN mkdir -p /app
EXPOSE 8083
CMD ["python3", "/app/src/main/python/server.py"]
