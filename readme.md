# Image Forgery Detection System

A Python-based desktop application that helps detect possible image manipulation using **Error Level Analysis (ELA)**, **Edge Detection**, and **EXIF Metadata Analysis**. The application provides an intuitive Tkinter-based graphical interface for uploading and analyzing digital images.

---

## 📌 Features

* Upload and analyze image files through a simple GUI.
* Perform **Error Level Analysis (ELA)** to identify regions that may have been modified.
* Detect image boundaries and inconsistencies using **Canny Edge Detection**.
* Extract and display **EXIF metadata** from images.
* View the original image, ELA result, and edge detection result side by side.
* Dark-themed user interface for improved usability.

---

## 🛠️ Technologies Used

* Python
* Tkinter
* OpenCV
* Pillow (PIL)
* NumPy

---

## 📂 Project Structure

```text
Image-Forgery-Detection-System/
│── csdf_mini.py          # Main application
│── requirements.txt      # Required Python libraries
│── README.md             # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/Image-Forgery-Detection-System.git
```

2. Navigate to the project folder.

```bash
cd Image-Forgery-Detection-System
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Run the application.

```bash
python csdf_mini.py
```

---

## 🚀 How It Works

1. Launch the application.
2. Select an image from your computer.
3. The application performs:

   * Error Level Analysis (ELA)
   * Edge Detection
   * Metadata Extraction
4. Review the generated outputs and metadata to identify possible signs of image manipulation.

---

## 📸 Output

The application displays:

* Original Image
* Error Level Analysis (ELA) Result
* Edge Detection Result
* EXIF Metadata Information

---

## 📖 Concepts Used

### Error Level Analysis (ELA)

ELA detects differences introduced during JPEG compression. Edited portions of an image often exhibit different compression levels, making potential tampering easier to identify.

### Edge Detection

The application uses the Canny Edge Detection algorithm to highlight edges and structural changes that may indicate image modifications.

### Metadata Analysis

Extracts available EXIF metadata such as camera information, timestamps, and other image properties that can assist in digital forensic analysis.

---

## 📌 Future Enhancements

* AI/Deep Learning-based forgery detection.
* Support for additional image formats.
* Automatic forgery probability scoring.
* Region highlighting for suspected tampered areas.
* Batch image analysis.
* Detailed forensic report generation.

---

## 👨‍💻 Author

Developed as a Computer Engineering mini project for learning the fundamentals of **Digital Image Forensics**, **Image Processing**, and **Python GUI Development**.
