# Base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the port for external access (if running as a web service)
EXPOSE 8080

# Define the command to run the application
CMD ["python", "app.py"]
