FROM python:3.9

COPY ./src/backend /app

RUN python3.9 -m venv /opt/venv

ENV PATH="/opt/venv/bin:${PATH}"
ENV VIRTUALENV=/opt/venv
ENV PYTHONPATH=/app

RUN apt install -y python3.9-dev libcairo2-dev pkg-config

RUN pip install -r /app/requirements/production.txt

WORKDIR /app/

CMD [ "uvicorn", "hortus.main:app" ]