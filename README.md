# Photo-Booth
# 📸 Webcam Photo Booth with Filters

This is a Python-based real-time webcam photo booth that allows users to apply various filters (like grayscale, blur, and sepia) and capture photos. Each photo's metadata—filter used, timestamp, and filename—is logged in a CSV file using Pandas.

---

## 🔧 Features

- Live webcam video feed with filters
- Toggle filters using keyboard
- Capture and save filtered photos
- Store photo metadata in a CSV log

---

## 🖼 Filters Available

- 🎨 Normal
- ⚫ Grayscale
- 💨 Blur
- 🌅 Sepia

---

## ⌨️ Controls

- Press **`f`** → Switch filter  
- Press **`s`** → Save photo  
- Press **`q`** → Quit the app  

---

## 📁 Output

- Photos saved in the `photos/` directory
- Log saved in `photo_log.csv` with:
  - Timestamp
  - Filter used
  - Filename

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install opencv-python pandas
```

## ▶️ Run the App
```sh
python photo_booth.py
```

## 📝 Sample Log (`photo_log.csv`)

| Time              | Filter    | Filename                          |
|------------------|-----------|-----------------------------------|
| 2025-04-25_180030 | sepia     | photos/photo_20250419_180030.jpg |
| 2025-04-25_180035 | grayscale | photos/photo_20250419_180035.jpg |

## 💡 Future Ideas
 -Add cartoon/sketch filters
 -GUI with buttons for easier control
 -Upload feature to share directly to social media
