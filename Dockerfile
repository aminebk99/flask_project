# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]
