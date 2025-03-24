FROM python:3.8-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

CMD ["python", "app.py"]
