FROM python:3.9


COPY . /app/.
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-u", "run.py"]