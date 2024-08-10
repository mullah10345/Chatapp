# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the application
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.py", "storyweave.wsgi:application"]
