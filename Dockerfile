# Use official Python slim image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    espeak-ng \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install CPU-only PyTorch from PyTorch wheels URL
# RUN pip install torch==2.1.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Install other Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set working directory
WORKDIR /app

# Copy your Kokoro script or your entire repo
COPY . .

# Default command (optional)
CMD ["python", "generate_kokoro_tts.py"]
