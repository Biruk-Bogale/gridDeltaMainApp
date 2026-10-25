def build_message(cutoff: str, bin_width: int) -> dict:
    return {"cutoff": cutoff, "binWidth": bin_width, "bins": 3000 // bin_width}
