# Use the official Python image
FROM python:3.9-slim

# Deploy the work directory
WORKDIR /app

# Copy all project files
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the application
CMD ["python", "main.py"]