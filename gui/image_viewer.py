import customtkinter as ctk
from vision.image_utils import load_image

class ImageViewer(ctk.CTkLabel):
    def __init__(self, master):
        super().__init__(master, text="")
        self.image_ref = None  # IMPORTANT: prevent garbage collection

    def show(self, image_path: str):
        pil_img = load_image(image_path)
        self.image_ref = ctk.CTkImage(
            light_image=pil_img,
            dark_image=pil_img,
            size=pil_img.size
        )
        self.configure(image=self.image_ref)
