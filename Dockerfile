# Choose python version
FROM python:3.11-slim-bookworm

# Create working folder
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install poetry
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false

# Install any necessary packages
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev

# Install Tesseract English language package
RUN apt-get install -y tesseract-ocr-eng

# Put requirements files into working directory
COPY pyproject.toml /app

# Install poetry requirements
RUN poetry install --no-interaction --no-ansi --no-root --without dev

COPY . /app

RUN pip install --no-cache-dir gradio

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python","main.py"]