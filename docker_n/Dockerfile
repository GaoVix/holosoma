FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

COPY . /app

RUN pip install -e /app/src/holosoma_retargeting

RUN pip install torch tqdm dotmap PyYAML omegaconf loguru

RUN pip install -e /app/src/holosoma_retargeting/holosoma_retargeting/data_utils/human_body_prior


CMD ["python", "--version"]
