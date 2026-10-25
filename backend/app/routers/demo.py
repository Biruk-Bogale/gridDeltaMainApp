from fastapi import APIRouter

from app.controllers import demo_controller

router = APIRouter(prefix="/api/v1", tags=["demo"])


@router.get("/echo")
def echo(cutoff: str = "09:00", bin_width: int = 250):
    return demo_controller.echo(cutoff, bin_width)
