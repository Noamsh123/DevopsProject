FROM python:3
COPY requirments.txt /
COPY app.py /
COPY db /db
RUN pip install -r requirments.txt
ENTRYPOINT [ "python3", "app.py" ]