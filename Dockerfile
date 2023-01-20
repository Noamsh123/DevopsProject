FROM python:3

# WORKDIR /usr/src/app

COPY requirments.txt /
COPY app.py /
COPY db /db
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysql-connector-python
RUN pip install -r requirments.txt
# EXPOSE 5000
# RUN python3 db/dbconnect.py
# mysql-connector-python==2.2.9
ENTRYPOINT [ "python3", "app.py" ]