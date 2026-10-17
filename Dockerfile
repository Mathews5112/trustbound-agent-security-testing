FROM python:3.11-slim

WORKDIR /app

COPY sandbox_check.py .

CMD ["python", "sandbox_check.py"]