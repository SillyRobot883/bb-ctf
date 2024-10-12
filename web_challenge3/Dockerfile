# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/
COPY .env .

# Expose port 80
EXPOSE 80

# Run the Flask app
CMD ["python", "app.py"]
