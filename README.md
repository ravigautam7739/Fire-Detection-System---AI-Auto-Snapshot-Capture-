# 🔥 Fire Detection System (AI + Auto Snapshot Capture)

A Python-based **Fire Detection System** that detects fire in real-time using your webcam and automatically captures snapshots when fire is detected.

This project simulates a **smart surveillance system** used in safety monitoring and emergency detection.

---

# 🚀 Features

✔ Real-time fire detection using webcam
✔ Detects fire based on color segmentation
✔ Highlights detected fire area
✔ Displays alert screen when fire is detected
✔ Automatically saves snapshots of fire events
✔ Cooldown system to avoid multiple captures

---

# 🛠 Technologies Used

* Python
* OpenCV
* NumPy
* Computer Vision (HSV color detection)

---

# 📂 Project Structure

```id="t9m3vl"
fire-detection-system
│
├── main.py
├── fire_snapshots/
└── README.md
```

👉 Rename your file to **main.py** for clean structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="p3n8kr"
pip install opencv-python numpy
```

---

# ▶️ How to Run

```bash id="z7k2mq"
git clone https://github.com/ravigautam7739/fire-detection-system.git
cd fire-detection-system
python main.py
```

---

# 🧠 How It Works

1. Webcam captures live video
2. Frame is converted to **HSV color space**
3. Fire-like colors (red/orange/yellow) are detected
4. Contours are analyzed to identify fire regions
5. If fire is detected:

   * Alert overlay appears
   * Bounding box is drawn
   * Snapshot is saved automatically

---

# 💻 Example Output

```id="x4n9pt"
FIRE DETECTED!

SNAPSHOT SAVED!
```

Saved images:

```id="u8p3wl"
fire_snapshots/fire_1712345678.jpg
```

---

# 🎯 Use Cases

* Fire safety monitoring
* Smart surveillance systems
* Industrial safety applications
* AI-based emergency detection
* Computer vision learning

---

# ⚠️ Notes

* Requires webcam
* Detection is based on color (may detect similar colors)
* Works best in controlled lighting
* Not a replacement for real fire safety systems

---

# 🔮 Future Improvements

* Smoke detection
* Temperature sensor integration
* Alarm system (sound alerts)
* Email/SMS notifications
* AI model-based fire detection

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and real-world automation projects**.

Stay tuned 🚀
