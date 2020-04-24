FROM python:3.7.7-alpine3.11
RUN pip install flask
RUN pip install flask_restful
RUN pip install mysql-connector
RUN pip3 install python-dateutil
RUN pip install pybuilder --pre
RUN pip3 install pyjwt
RUN pip3 install crypto
RUN mkdir -p /app
EXPOSE 8083
CMD ["python3", "/app/src/main/python/server.py"]
