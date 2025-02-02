# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . /app/

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app using gunicorn (production WSGI server)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
