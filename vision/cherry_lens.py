from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from pathlib import Path


class CherryLens:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

    def analyze_images(self, image_paths):
        """
        Takes list of image paths and returns list of captions.
        """
        captions = []

        for path in image_paths:
            img_path = Path(path)
            if not img_path.exists():
                continue

            image = Image.open(img_path).convert("RGB")
            inputs = self.processor(image, return_tensors="pt").to(self.device)

            with torch.no_grad():
                output = self.model.generate(**inputs, max_new_tokens=50)

            caption = self.processor.decode(output[0], skip_special_tokens=True)
            captions.append(caption)

        return captions
