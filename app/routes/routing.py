from fastapi import APIRouter, HTTPException, Query, Depends
from app.services.osrm_service import get_route
from app.dependencies import verify_api_key
from typing import Tuple

router = APIRouter()

@router.get("/route")
async def route(
    origin: str = Query(..., regex="^-?\d+(\.\d+)?,-?\d+(\.\d+)?$"),
    destination: str = Query(..., regex="^-?\d+(\.\d+)?,-?\d+(\.\d+)?$"),
    api_key: str = Depends(verify_api_key)
):
    origin_lat, origin_lon = map(float, origin.split(','))
    dest_lat, dest_lon = map(float, destination.split(','))
    
    distance, duration = await get_route(origin_lat, origin_lon, dest_lat, dest_lon)
    
    if distance is None or duration is None:
        raise HTTPException(status_code=503, detail="OSRM service is unavailable or unable to calculate route")
    
    hours, minutes = divmod(int(duration), 60)
    duration_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"
    
    return {
        "code": "Ok",
        "distance": f"{distance:.2f} km",
        "duration": duration_str
    }