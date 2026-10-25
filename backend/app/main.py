from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.errors import AppError
from app.routers import demo

app = FastAPI(title="Grid Delta Portal", version="0.1.0")
app.include_router(demo.router)


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": exc.code, "message": exc.message}},
    )


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
