from app.core.errors import AppError
from app.services import demo_service


def echo(cutoff: str, bin_width: int) -> dict:
    if not 50 <= bin_width <= 1000:
        raise AppError(400, "VALIDATION_ERROR", "binWidth must be between 50 and 1000")
    return demo_service.build_message(cutoff, bin_width)



