from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.routes import routing
from app.config import settings

app = FastAPI(title="OSRM Mali Backend")

app.include_router(routing.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"code": "Bad Request", "detail": str(exc)},
    )

@app.get("/")
async def root():
    return {"message": "Welcome to OSRM Mali Backend"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)