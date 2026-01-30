from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path

MODEL_DIR = Path("CherryAI/models/sd15")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)

pipe.save_pretrained(MODEL_DIR)

print("✅ Stable Diffusion 1.5 downloaded successfully into CherryAI/models/sd15")
