# PhotoGallery — Private Local Photo Manager

PhotoGallery is a **modern, privacy-first photo management application** built with **Python (Flask) and SQLite**.  
It provides a Google Photos–like experience **entirely offline**, running locally on your machine and accessed through your web browser.

All photos and data stay on your system.  
There is **no cloud**, **no tracking**, and **no external services**.

---

## ✨ Features

### 🔐 Secure Local Accounts
- Username & password authentication
- Passwords securely hashed
- No internet dependency
- Each user sees only their own photos

### 🖼️ Modern Gallery Experience
- Futuristic dark UI with glassmorphism
- AI-style masonry layout (Google Photos / Pinterest feel)
- Smooth animations and transitions
- Responsive across screen sizes

### 🔍 Advanced Fullscreen Viewer
- Fullscreen photo viewing
- Swipe left/right (mouse, keyboard, touch)
- Mouse wheel & pinch-to-zoom
- Keyboard navigation (`←`, `→`, `Esc`)

### 🧠 Smart Organization
- **Timeline grouping**: Today / Yesterday / Earlier
- **Smart Albums**:
  - 📸 Camera
  - 📱 Screenshots
  - ⬇️ Downloads
- Instant regrouping (no reload)
- Offline & privacy-safe logic

### ⬆️ Upload & Management
- Multi-image upload
- Real upload progress bar
- Secure photo deletion
- Local filesystem storage
- SQLite metadata database

---

## 🧰 Technology Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python (Flask) |
| Database | SQLite (hardened connection layer) |
| Frontend | HTML, CSS, JavaScript |
| UI Icons | Google Material Icons |
| Storage | Local filesystem |

---

## 🔒 Privacy & Ethics

PhotoGallery is designed with privacy as a core principle:

- No cloud uploads
- No analytics or telemetry
- No face recognition storage
- No biometric data retention
- All processing happens locally on your device

---

## 📂 Project Structure

photo_gallery/
│── app.py
│── database.db # auto-created
│
├── uploads/ # user images
│
├── templates/
│ ├── login.html
│ ├── signup.html
│ └── gallery.html
│
└── static/
├── material.css
├── icons.css
├── transitions.js
├── viewer.js
├── upload.js
└── smart-albums.js



---

## ▶️ Run Locally (Development / Personal Use)

### Requirements
- Python 3.9+
- pip

### Install Dependencies
```bash
pip install flask werkzeug

Start the App
python app.py

Open in Browser
http://127.0.0.1:5000


The app runs locally only and does not expose itself to the internet.


🧪 First-Time Setup Note

If you tested older versions:

Stop the app

Delete database.db

Restart the app

Create a new account

🎯 Use Cases

Personal photo management

Offline photo library

Privacy-conscious users

Learning reference for Flask applications

Open-source photo gallery projects

📌 Roadmap (Optional Enhancements)

Timeline scrubber

EXIF-based camera detection

Color-based smart albums

Offline-first caching

Multi-user admin tools

📄 License

This project is intended for open-source and personal use.

🙌 Contributions

Contributions, ideas, and improvements are welcome.
Please fork the repository and submit a pull request.

⭐ Acknowledgements

Inspired by modern photo gallery experiences while prioritizing
privacy, simplicity, and full local control.


---

If you want next, I can:
- Add screenshots section to README
- Write `CONTRIBUTING.md`
- Add `.gitignore`
- Prepare MIT license
- Clean the repo for first GitHub release

Just tell me what to do next.
