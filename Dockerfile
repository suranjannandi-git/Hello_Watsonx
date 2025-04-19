# Use the official Python 3.12 base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install requirements
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install vim (advanced vi editor)
RUN apt update && apt install vim -y

# Expose the port the app runs on
EXPOSE 8080

# Set the default command to run the app
CMD ["python3", "call_wx_restapi.py"]
