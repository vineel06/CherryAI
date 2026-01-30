import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models" / "sd15"
OUTPUT_DIR = BASE_DIR / "output" / "images"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🍒 Loading Stable Diffusion (Cherry Vision Engine)...")

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_DIR,
    torch_dtype=torch.float16,
    safety_checker=None
)

pipe = pipe.to("cuda")
pipe.enable_attention_slicing()

print("✅ Cherry Vision Engine ready")

# -------------------------------
# SMART PROMPT ENGINE
# -------------------------------

BASE_STYLE = (
    "ultra realistic, high detail, sharp focus, cinematic lighting, "
    "perfect anatomy, symmetrical face, realistic human proportions, "
    "8k detail, professional photography"
)

NEGATIVE_STYLE = (
    "blurry, distorted, deformed, mutated, extra limbs, extra fingers, "
    "bad anatomy, cross-eyed, ugly, cartoon, anime, low quality, monkey, alien"
)

def generate_image(user_prompt: str) -> str:
    """
    Generates a realistic image using optimized prompt engineering.
    """

    final_prompt = f"{user_prompt}, {BASE_STYLE}"

    print(f"🎨 Cherry drawing: {user_prompt}")

    image = pipe(
        prompt=final_prompt,
        negative_prompt=NEGATIVE_STYLE,
        num_inference_steps=30,
        guidance_scale=8.5,
        width=512,
        height=512
    ).images[0]

    filename = f"cherry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = OUTPUT_DIR / filename
    image.save(path)

    print(f"✅ Image saved: {path}")
    return str(path)
