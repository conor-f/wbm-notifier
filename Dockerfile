# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir .

# Set environment variables for configuration
ENV URL
ENV SHELF_PATH
ENV TOPIC
ENV NTFY_SERVER
ENV CHECK_INTERVAL

# Command to run the package
CMD ["wbm-notifier"]
