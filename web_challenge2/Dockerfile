FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the app files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the port the app will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
