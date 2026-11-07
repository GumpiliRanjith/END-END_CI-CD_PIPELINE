FROM python:3.12-slim
WORKDIR /app
COPY python3.py .
CMD ["python", "python3.py"]