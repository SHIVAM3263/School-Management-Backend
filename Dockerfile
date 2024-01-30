FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 7755 available to the world outside this container
EXPOSE 7755

# Define environment variable
ENV FLASK_APP=core/server.py

# Run app.py when the container launches
CMD ["gunicorn", "-c", "gunicorn_config.py", "core.server:app"]
