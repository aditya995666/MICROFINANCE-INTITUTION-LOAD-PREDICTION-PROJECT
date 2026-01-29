FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir \
    streamlit \
    pandas \
    joblib \
    scikit-learn \
    xgboost \
    imbalanced-learn \
    PyPDF2 \
    reportlab

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
