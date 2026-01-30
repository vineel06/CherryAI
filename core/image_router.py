from pathlib import Path

IMAGE_OUTPUT_DIR = Path("outputs/images")

def latest_image():
    images = sorted(IMAGE_OUTPUT_DIR.glob("*.png"), key=lambda x: x.stat().st_mtime)
    return str(images[-1]) if images else None
