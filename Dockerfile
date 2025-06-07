# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, depends on your app)
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py"]
