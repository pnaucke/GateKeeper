FROM python:3.10-slim

WORKDIR /app

COPY Gatekeeper.py .

CMD ["python", "Gatekeeper.py"]

# Installeer Flask
RUN pip install flask

EXPOSE 5000