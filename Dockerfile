# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if your bot interacts with a web server)
# EXPOSE 8080

# Add the environment variables file
# Ensure your .env file is copied if it is required at runtime
COPY .env /app/.env

# Define the command to run your bot
CMD ["python", "main.py"]
