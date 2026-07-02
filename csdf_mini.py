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
