from PIL import Image

def load_image(path: str, max_size=(512, 512)) -> Image.Image:
    img = Image.open(path).convert("RGB")
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img
