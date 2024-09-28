# OSRM Mali Backend

## Overview

OSRM Mali Backend is a FastAPI-based service that provides routing capabilities for Mali using OpenStreetMap data and the OSRM (Open Source Routing Machine) engine. This service offers an HTTP API endpoint for calculating routes between two points in Mali.

## Features

- Route calculation between two geographic coordinates
- Distance and duration estimation for routes
- API key authentication for secure access
- Dockerized application for easy deployment
- Built on FastAPI for high performance and easy API documentation

## Prerequisites

- Docker
- Docker Compose (optional, for easier management)

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/mali-route-backend.git
   cd mali-route-backend
   ```

2. Create a `.env` file in the root directory and set your API key:
   ```
   API_KEY=your_secret_api_key_here
   ```

3. Build and run the Docker container:
   ```
   docker build -t mali-route-backend .
   docker run -p 8000:8000 -p 5001:5001 mali-route-backend
   ```

   Alternatively, if you're using Docker Compose:
   ```
   docker-compose up --build
   ```

4. The service will be available at `http://localhost:8000`.

## API Documentation

### Authentication

All API requests require an API key to be sent in the `X-API-Key` header.

### Endpoints

#### GET /route

Calculate a route between two points.

**Parameters:**

- `origin` (required): Comma-separated latitude and longitude of the starting point.
- `destination` (required): Comma-separated latitude and longitude of the end point.

**Headers:**

- `X-API-Key` (required): Your API key for authentication.

**Example Request:**

```
curl -H "X-API-Key: your_api_key_here" "http://localhost:8000/route?origin=12.65,-8.0&destination=13.5,-7.5"
```

**Example Response:**

```json
{
  "code": "Ok",
  "distance": "120.5 km",
  "duration": "2h 15m"
}
```

**Error Responses:**

- 400 Bad Request: Invalid input parameters
- 403 Forbidden: Invalid API key
- 503 Service Unavailable: OSRM service is unavailable or unable to calculate route

#### GET /health

Check the health status of the service.

**Example Request:**

```
curl "http://localhost:8000/health"
```

**Example Response:**

```json
{
  "status": "healthy"
}
```

## Development

### Project Structure

```
mali-route-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── dependencies.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── routing.py
│   └── services/
│       ├── __init__.py
│       └── osrm_service.py
│
├── Dockerfile
├── requirements.txt
├── run.sh
└── README.md
```

### Configuration

Configuration is managed through environment variables and the `config.py` file. The following settings are available:

- `OSRM_URL`: URL of the OSRM routing engine (default: "http://localhost:5001")
- `LOG_LEVEL`: Logging level (default: "INFO")
- `API_KEY`: Secret key for API authentication
