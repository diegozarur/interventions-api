# Use the official Python 2.7 image
FROM python:2.7

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application with auto-reload
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000", "--reload"]
