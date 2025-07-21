import tkinter as tk
from tkinter import ttk

from gui.encode_tab import EncodeTab
from gui.decode_tab import DecodeTab
from gui.convert_tab import ConvertTab

def main():
    root = tk.Tk()
    root.title("🕵️ Steganography Tool")
    root.configure(bg="#111827")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook", background="#111827", borderwidth=0)
    style.configure("TNotebook.Tab", background="#1f2937", foreground="white", padding=10)
    style.map("TNotebook.Tab", background=[("selected", "#374151")])
    style.configure("TFrame", background="#111827")
    style.configure("TLabel", background="#111827", foreground="white", font=("Segoe UI", 10))
    style.configure("TButton", background="#4b5563", foreground="white", padding=6)
    style.map("TButton", background=[("active", "#6b7280")])

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=20, pady=20)

    encode_tab = EncodeTab(notebook)
    decode_tab = DecodeTab(notebook)
    convert_tab = ConvertTab(notebook)

    notebook.add(encode_tab, text="🖼️ Encode")
    notebook.add(decode_tab, text="🗃️ Decode")
    notebook.add(convert_tab, text="🖼️ Convert to PNG")

    root.mainloop()

if __name__ == "__main__":
    main()
