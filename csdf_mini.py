# forgery_ui_orange_fixed_multi.py
import cv2
import numpy as np
from PIL import Image, ImageTk, ExifTags
import tkinter as tk
from tkinter import filedialog, messagebox
import os


# ------------------------ CONFIG ------------------------
ELA_OUTPUT = "ela_result.jpg"
EDGES_OUTPUT = "edges_result.jpg"
TEMP_ELA = "temp_ela.jpg"
PREVIEW_SIZE = (350, 350)


# ------------------------ CORE ANALYSIS FUNCTIONS ------------------------
def error_level_analysis(image_path, temp_filename=TEMP_ELA, quality=90):
    original = Image.open(image_path).convert("RGB")
    original.save(temp_filename, "JPEG", quality=quality)
    compressed = Image.open(temp_filename).convert("RGB")

    diff = np.abs(np.asarray(original, dtype=np.int16) - np.asarray(compressed, dtype=np.int16))
    extrema = diff.max()
    scale = 255.0 / extrema if extrema != 0 else 1.0
    diff = (diff * scale).astype(np.uint8)
    ela_image = Image.fromarray(diff)

    try:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
    except Exception:
        pass
    return ela_image.convert("RGB")

def metadata_analysis(image_path):
    exif_data = {}
    try:
        image = Image.open(image_path)
        if hasattr(image, "_getexif") and image._getexif():
            for tag, value in image._getexif().items():
                name = ExifTags.TAGS.get(tag, tag)
                exif_data[name] = value
    except Exception:
        return {}
    return exif_data

def edge_analysis(image_path):
    img_cv = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img_cv is None:
        raise FileNotFoundError(f"cv2 could not read image: {image_path}")
    edges = cv2.Canny(img_cv, 100, 200)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return Image.fromarray(edges_rgb)


# ------------------------ GUI SETUP ------------------------
root = tk.Tk()
root.title("🧠 Image Forgery Detection (Orange Theme)")
root.geometry("1200x750")
root.config(bg="#1c1a17")
root.resizable(False, False)

title = tk.Label(root, text="🔍 Image Forgery Detection System",
                 bg="#1c1a17", fg="#f4a261", font=("Arial", 22, "bold"))
title.pack(pady=12)

frame_buttons = tk.Frame(root, bg="#1c1a17")
frame_buttons.pack(pady=6)

selected_images = []  # store multiple paths
