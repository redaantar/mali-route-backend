FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    pkg-config \
    libbz2-dev \
    libxml2-dev \
    libzip-dev \
    libboost-all-dev \
    lua5.2 \
    liblua5.2-dev \
    libtbb-dev \
    python3 \
    python3-pip \
    wget

WORKDIR /osrm
RUN wget https://github.com/Project-OSRM/osrm-backend/archive/v5.26.0.tar.gz \
    && tar -xzvf v5.26.0.tar.gz \
    && cd osrm-backend-5.26.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && cmake --build . \
    && cmake --build . --target install

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app
COPY .env /app/.env

COPY . /app

EXPOSE 8000

ENV OSRM_URL=http://localhost:5001

RUN wget http://download.geofabrik.de/africa/mali-latest.osm.pbf

RUN osrm-extract -p /usr/local/share/osrm/profiles/car.lua mali-latest.osm.pbf
RUN osrm-partition mali-latest.osrm
RUN osrm-customize mali-latest.osrm

RUN echo '#!/bin/bash\n\
osrm-routed --algorithm mld /app/mali-latest.osrm --port 5001 &\n\
uvicorn app.main:app --host 0.0.0.0 --port 8000\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]