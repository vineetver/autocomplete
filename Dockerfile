FROM quay.io/fedora/python-310

WORKDIR /app

# Copy and install dependencies
# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Expose the port the app runs on
EXPOSE 5000

CMD ["python", "main.py"]

