from pathlib import Path
import shutil

BASE_UPLOAD = Path("uploads")
IMAGE_DIR = BASE_UPLOAD / "images"
FILE_DIR = BASE_UPLOAD / "files"

IMAGE_DIR.mkdir(parents=True, exist_ok=True)
FILE_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

def handle_upload(file_path: str) -> tuple[str, str]:
    src = Path(file_path)
    ext = src.suffix.lower()

    if ext in IMAGE_EXTS:
        dst = IMAGE_DIR / src.name
        shutil.copy(src, dst)
        return "image", str(dst)

    dst = FILE_DIR / src.name
    shutil.copy(src, dst)
    return "file", str(dst)
