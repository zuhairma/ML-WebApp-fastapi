# House Price Prediction Application

A tiny ML + web demo that predicts house prices from square footage.

## What’s in this repo

- `model-creation.py` — trains a simple Linear Regression model and writes `model.pkl`
- `main.py` — FastAPI app that loads `model.pkl` and serves a small HTML form

## Prerequisites

- Python 3.8+ (3.10+ recommended)

## Setup (Windows)

Create and activate a virtual environment:

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn scikit-learn numpy joblib
```

## Run

1) Train / generate the model file:

```bash
python model-creation.py
```

This creates `model.pkl` in the project folder.

2) Start the web app:

```bash
uvicorn main:app --reload
```

Open: http://127.0.0.1:8000

## Endpoints

- `GET /` — HTML form
- `POST /predict` — returns an HTML page with the predicted price

## Notes

- You must run `model-creation.py` before starting the API, otherwise `main.py` cannot load `model.pkl`.
- The HTML references `/static/favicon.ico`. It’s optional; the app works without it.
