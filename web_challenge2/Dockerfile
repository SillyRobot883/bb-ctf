# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . .

# Expose port 8002
EXPOSE 8002

# Command to run the application
CMD ["python", "app.py"]
