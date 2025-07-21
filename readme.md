# Steganography Tool

‍‍‍
**Author:** Setayesh SoheilNezhad
**GitHub:** [sin-soheili](https://github.com/sin-soheili)
**edX:**[S-soheili](https://profile.edx.org/u/S-soheili)
**Location:** Gorgan, Golestan Province, Iran
**date:** 2025-07-21

---

## Project Overview

This project is a user-friendly graphical steganography tool built with Python, designed to hide secret text messages inside images, extract hidden messages from images, and convert various image formats to PNG. Steganography is a technique for embedding secret data within ordinary files—in this case, images—without noticeable changes to the image itself.

The tool uses a simple but effective method of hiding text by manipulating the least significant bits (LSB) of the pixels in an image. This ensures the hidden message is imperceptible to the naked eye, providing a basic but practical approach to secret communication.

The project is implemented using Tkinter for the user interface, Pillow for image processing, and NumPy for efficient pixel manipulation. It’s modular, making it easy to understand, maintain, and extend.

---

## Features

* **Encode Text into Images:** Users can select any PNG image and embed their secret text into it. The text is converted into a binary sequence and hidden in the least significant bits of the image pixels.
* **Decode Text from Images:** The tool can extract hidden messages from images encoded with this method, recovering the original text.
* **Convert Images to PNG:** Users can convert images from formats like JPEG, BMP, WEBP, and others into PNG, which is necessary since the encoding and decoding require PNG images for lossless quality.
* **User-Friendly GUI:** A clean, modern interface with three tabs — Encode, Decode, and Convert — each with intuitive controls.
* **Custom Output Path Selection:** Users can choose where to save their output files, making the workflow flexible and convenient.

---

## Project Structure

* **`main.py`**
  The main entry point of the application. It initializes the GUI and coordinates between the different modules.

* **`steg_logic.py`**
  Contains the core steganography logic: functions for converting text to binary, hiding text in images, extracting text, and handling binary conversions.

* **`gui/encode_tab.py`**
  Implements the Encode tab UI and handles user inputs for hiding text into images.

* **`gui/decode_tab.py`**
  Implements the Decode tab UI and handles user inputs for extracting text from images.

* **`gui/convert_tab.py`**
  Implements the Convert tab UI for image format conversion to PNG.

* **`gui/__init__.py`**
  Makes the `gui` directory a package.

---

## Design Rationale

The application emphasizes clarity and modularity:

* **Modularity:** Each tab and core functionality is separated into different files to keep code organized and maintainable.
* **User Experience:** Tkinter’s notebook widget is used for easy navigation between encode, decode, and convert functions.
* **File Handling:** To avoid file overwrite and confusion, users select both input and output paths.
* **Simplicity:** The LSB steganography method is simple to understand yet effective for learning purposes.
* **Extensibility:** The project can be extended to support other file types, encryption, or more advanced steganography algorithms.

---

## How to Run

1. Make sure Python 3.x is installed.
2. Install dependencies:

   ```bash
   pip install pillow numpy
   ```
3. Run the application:

   ```bash
   python main.py
   ```
4. Use the GUI to select images and either hide text, extract text, or convert images.

---

## Video Tutorial

I have created a step-by-step video tutorial explaining the project setup, how to use the tool, and the underlying code logic. You can watch it here:

**[YouTube Video](https://youtu.be/wvBCzq1HGRc?si=39YOKYijhW5MGdhW)**


---

## Screen Shots

### Encode
![Encode](screenshots/encode.png)

### Decode
![Decode](screenshots/decode.png)

### Convert
![Convert](screenshots/convert.png)

### Example Output
![Example](screenshots/example.png)

