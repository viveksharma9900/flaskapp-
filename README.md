# Flask REST API with Docker & CI/CD

A REST API built with Python Flask, containerized 
with Docker, and deployed with GitHub Actions CI/CD.

## Endpoints
- GET / → Hello from Flask API!
- GET /health → Server is running!
- GET /predict → BERT Model status & accuracy

## Tech Stack
- Python + Flask
- Docker
- GitHub Actions CI/CD
- REST API

## Run Locally
pip install flask
python app.py

## Run with Docker
docker build -t flaskapp .
docker run -p 5000:5000 flaskapp
