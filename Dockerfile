FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pipenv

# Copy the pipenv install requirements from trading-backend to the working dir
COPY ./trading-backend/Pipfile ./trading-backend/Pipfile.lock /app/

# Install pipenv dependencies
RUN pipenv install --deploy --system

# Copy the rest of the app files to the working dir
COPY ./trading-backend ./trading-backend

# Run the app
CMD ["python", "-u", "trading-backend/src/BacktestDb.py"]
