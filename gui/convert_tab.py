import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image

class ConvertTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.convert_image_path = tk.StringVar()
        self.convert_output_path = tk.StringVar()

        ttk.Label(self, text="Select image to convert:").pack(pady=5)
        ttk.Button(self, text="📁 Browse Image", command=self.browse_convert_image).pack()
        ttk.Label(self, textvariable=self.convert_image_path, wraplength=400).pack()

        ttk.Button(self, text="📁 Select Output Path", command=self.select_convert_output_path).pack(pady=5)
        ttk.Label(self, textvariable=self.convert_output_path, wraplength=400).pack()

        ttk.Button(self, text="🔄 Convert to PNG", command=self.convert_image_to_png).pack(pady=10)

    def browse_convert_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.bmp *.webp *.png")])
        if path:
            self.convert_image_path.set(path)

    def select_convert_output_path(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Select output image file"
        )
        if path:
            self.convert_output_path.set(path)

    def convert_image_to_png(self):
        img_path = self.convert_image_path.get()
        output = self.convert_output_path.get()

        if not img_path or not output:
            messagebox.showerror("❌ Error", "Both input image and output path are required!")
            return

        if not output.lower().endswith(".png"):
            output += ".png"

        try:
            img = Image.open(img_path).convert("RGB")
            img.save(output, "PNG")
            messagebox.showinfo("✅ Success", f"Image successfully converted to {output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
