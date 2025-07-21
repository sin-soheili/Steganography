import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from steg_logic import extract_text

class DecodeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.decode_image_path = tk.StringVar()

        ttk.Label(self, text="Select image to extract text from:").pack(pady=5)
        ttk.Button(self, text="📁 Browse Image", command=self.browse_decode_image).pack()
        ttk.Label(self, textvariable=self.decode_image_path, wraplength=400).pack()

        ttk.Button(self, text="🔍 Decode", command=self.decode_text_from_image).pack(pady=10)
        self.decoded_result = tk.Text(self, height=8, width=50, bg="#1f2937", fg="white", state="disabled")
        self.decoded_result.pack(pady=5)

    def browse_decode_image(self):
        path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if path:
            self.decode_image_path.set(path)

    def decode_text_from_image(self):
        img_path = self.decode_image_path.get()
        if not img_path:
            messagebox.showerror("❌ Error", "Please select an image.")
            return

        try:
            result = extract_text(img_path)
            self.decoded_result.config(state="normal")
            self.decoded_result.delete("1.0", "end")
            self.decoded_result.insert("1.0", result)
            self.decoded_result.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))
