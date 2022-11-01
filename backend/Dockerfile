FROM python:3.10.8-slim
WORKDIR /workspace
COPY ./requirements.txt ./main.py ./
RUN python -m pip install -r ./requirements.txt
CMD gunicorn main:app \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8081
