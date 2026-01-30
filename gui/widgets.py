import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from core.brain import Brain


class ChatWidgets:
    def __init__(self, app):
        self.app = app
        self.brain = Brain()
        self.attachments = []
        self.previews = []

        self.chat_box = ctk.CTkTextbox(app, wrap="word", state="disabled", height=320)
        self.chat_box.pack(fill="both", expand=True, padx=10, pady=10)

        # Preview frame
        self.preview_frame = ctk.CTkFrame(app)
        self.preview_frame.pack(fill="x", padx=10, pady=(0, 5))

        bottom = ctk.CTkFrame(app)
        bottom.pack(fill="x", padx=10, pady=10)

        self.add_btn = ctk.CTkButton(
            bottom, text="+", width=40, command=self.add_files
        )
        self.add_btn.pack(side="left", padx=(0, 8))

        self.entry = ctk.CTkEntry(bottom, placeholder_text="Ask Cherry...")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.entry.bind("<Return>", self._on_enter)

        self.send_btn = ctk.CTkButton(bottom, text="Send", command=self.send_message)
        self.send_btn.pack(side="right")

        self._write("Cherry AI is ready 🍒\n")

    def _write(self, text):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", text)
        self.chat_box.see("end")
        self.chat_box.configure(state="disabled")

    def _on_enter(self, event):
        self.send_message()

    def clear_previews(self):
        for widget in self.preview_frame.winfo_children():
            widget.destroy()
        self.previews.clear()

    def add_files(self):
        files = filedialog.askopenfilenames(
            title="Add images",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.webp")]
        )
        if not files:
            return

        self.attachments = list(files)
        self.clear_previews()

        for path in self.attachments:
            img = Image.open(path).resize((80, 80))
            thumb = ctk.CTkImage(img, size=(80, 80))
            lbl = ctk.CTkLabel(self.preview_frame, image=thumb, text="")
            lbl.image = thumb
            lbl.pack(side="left", padx=5)

    def send_message(self):
        text = self.entry.get().strip()
        if not text:
            return

        self.entry.delete(0, "end")
        self._write(f"You: {text}\n")
        self._write("Cherry: thinking...\n")

        try:
            reply = self.brain.think(text, self.attachments)
        except Exception as e:
            reply = f"Error: {e}"

        self._write(f"{reply}\n\n")
        self.attachments = []
        self.clear_previews()
