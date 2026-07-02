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
