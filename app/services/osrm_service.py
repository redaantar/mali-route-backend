import aiohttp
from app.config import settings
import logging
from aiohttp.client_exceptions import ClientConnectorError

logger = logging.getLogger(__name__)

async def get_route(start_lat: float, start_lon: float, end_lat: float, end_lon: float):
    url = f"{settings.OSRM_URL}/route/v1/driving/{start_lon},{start_lat};{end_lon},{end_lat}"
    
    logger.info(f"Attempting to connect to OSRM backend at: {url}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                
                if data["code"] != "Ok":
                    logger.error(f"OSRM error: {data['code']}")
                    return None, None
                
                route = data["routes"][0]
                distance = route["distance"] / 1000  # Convert to kilometers
                duration = route["duration"] / 60  # Convert to minutes
                
                if distance == 0 and duration == 0:
                    logger.warning("Route found, but distance and duration are zero.")
                    return None, None
                
                logger.info(f"Successfully retrieved route. Distance: {distance:.2f} km, Duration: {duration:.2f} min")
                return distance, duration
    except ClientConnectorError as e:
        logger.error(f"Unable to connect to OSRM backend: {e}")
        logger.error(f"OSRM URL: {settings.OSRM_URL}")
        return None, None
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return None, None