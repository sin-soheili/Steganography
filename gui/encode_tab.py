import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from steg_logic import hide_text

class EncodeTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.encode_image_path = tk.StringVar()
        self.encode_output_path = tk.StringVar()
        self.encode_text = tk.Text(self, height=5, width=50, bg="#1f2937", fg="white", insertbackground="white")

        ttk.Label(self, text="Select image to hide text into:").pack(pady=5)
        ttk.Button(self, text="📁 Browse Image", command=self.browse_encode_image).pack()
        ttk.Label(self, textvariable=self.encode_image_path, wraplength=400).pack()

        ttk.Label(self, text="Enter text to hide:").pack(pady=5)
        self.encode_text.pack(pady=5)

        ttk.Button(self, text="📁 Select Output Path", command=self.select_encode_output_path).pack(pady=5)
        ttk.Label(self, textvariable=self.encode_output_path, wraplength=400).pack()

        ttk.Button(self, text="🛠️ Encode", command=self.encode_text_to_image).pack(pady=10)

    def browse_encode_image(self):
        path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if path:
            self.encode_image_path.set(path)

    def select_encode_output_path(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Select output image file"
        )
        if path:
            self.encode_output_path.set(path)

    def encode_text_to_image(self):
        img_path = self.encode_image_path.get()
        text = self.encode_text.get("1.0", "end-1c")
        output = self.encode_output_path.get()

        if not img_path or not text or not output:
            messagebox.showerror("❌ Error", "All fields are required!")
            return

        try:
            hide_text(img_path, text, output)
            messagebox.showinfo("✅ Success", f"Text hidden successfully in {output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
