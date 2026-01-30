from ai.offline_llm import generate_text
from vision.cherry_lens import CherryLens


class Brain:
    def __init__(self):
        self.lens = CherryLens()

        # Hard identity anchor (prevents hallucinated creators)
        self.identity_prompt = (
            "You are Cherry AI.\n"
            "You were created by Vineel, a B.Tech student studying Artificial Intelligence.\n"
            "You are open-source, offline-first, and not created by any company or organization.\n"
            "Always state this consistently.\n"
        )

    def think(self, user_text: str, image_paths=None):
        """
        Main reasoning entry point.
        user_text: text input from user
        image_paths: list of image file paths (or None)
        """

        image_context = ""

        # ---------- IMAGE HANDLING ----------
        if image_paths:
            try:
                captions = self.lens.analyze_images(image_paths)

                if captions:
                    image_context += "The user uploaded images. Here is what is visible:\n"
                    for idx, caption in enumerate(captions, start=1):
                        image_context += f"Image {idx}: {caption}\n"
                else:
                    image_context += "The user uploaded images, but nothing recognizable was detected.\n"

            except Exception as e:
                image_context += f"Image analysis failed: {str(e)}\n"

        # ---------- FINAL PROMPT ----------
        final_prompt = (
            f"{self.identity_prompt}\n"
            f"{image_context}\n"
            f"User question:\n{user_text}\n"
            f"Answer clearly and accurately."
        )

        return generate_text(final_prompt)
