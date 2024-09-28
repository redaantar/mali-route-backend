# OSRM Mali Backend

## Overview

OSRM Mali Backend is a FastAPI-based web service that provides routing information for Mali using OpenStreetMap data and the OSRM (Open Source Routing Machine) engine. This service offers an API endpoint for calculating routes between two points in Mali, returning distance and duration information.

## Features

- Route calculation between two geographical points in Mali
- Distance and duration estimation for routes
- API key authentication for secure access
- Dockerized application for easy deployment
- Integration with OSRM for efficient routing calculations

## Prerequisites

- Docker
- Docker Compose (optional, for easier management)
- Mali OSM data (automatically downloaded in the Dockerfile)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/osrm-mali-backend.git
   cd osrm-mali-backend
   ```

2. Create a `.env` file in the root directory with the following content:
   ```
   OSRM_URL=http://localhost:5001
   LOG_LEVEL=INFO
   API_KEY=your_secret_api_key_here
   ```
   Replace `your_secret_api_key_here` with a strong, unique API key.

3. Build and run the Docker container:
   ```
   ./run.sh
   ```
   This script will build the Docker image and start the container, exposing the FastAPI application on port 8000 and the OSRM backend on port 5001.

   PS: If the command `./run.sh` doesn't work, try the following command:
   ```
   chmod +x run.sh
   ```
   Then, run `./run.sh` again.

## Usage

To use the API, send a GET request to the `/route` endpoint with the following query parameters:

- `origin`: The starting point of the route (format: `latitude,longitude`)
- `destination`: The ending point of the route (format: `latitude,longitude`)

Include the API key in the `X-API-Key` header.

Example using curl:

```
curl -H "X-API-Key: your_secret_api_key_here" "http://localhost:8000/route?origin=12.65,-8.0&destination=13.5,-7.5"
```

The API will respond with a JSON object containing the route distance and duration:

```json
{
  "code": "Ok",
  "distance": "150.25 km",
  "duration": "2h 15m"
}
```

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `GET /route`: Route calculation endpoint (requires authentication)

## Project Structure

```
osrm-mali-backend/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── dependencies.py
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routing.py
│   └── services/
│       ├── __init__.py
│       └── osrm_service.py
├── Dockerfile
├── requirements.txt
├── run.sh
├── .env
└── README.md
```

## Configuration

The application can be configured using environment variables or the `.env` file. The following settings are available:

- `OSRM_URL`: URL of the OSRM backend service (default: `http://localhost:5001`)
- `LOG_LEVEL`: Logging level (default: `INFO`)
- `API_KEY`: Secret API key for authentication

## Deployment

The application is containerized using Docker, making it easy to deploy to various environments. Adjust the `Dockerfile` and `run.sh` script as needed for your specific deployment requirements.