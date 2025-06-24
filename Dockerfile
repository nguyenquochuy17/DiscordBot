FROM python:3.12-slim

# Install system packages
RUN apt update && apt install -y ffmpeg libopus0

# Set workdir
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run app
CMD ["python", "app.py"]
