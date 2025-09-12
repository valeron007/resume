FROM python:3.13.5
USER root
COPY ./ /backend

WORKDIR /backend

RUN pip install pip-tools
RUN pip-compile
RUN pip-sync

# RUN alembic upgrade 159c582c0a4f

EXPOSE 8080

CMD ["python3", "app.py"]

