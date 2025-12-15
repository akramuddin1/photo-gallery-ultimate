# PhotoGallery — Private Desktop Photo Manager (Windows)

PhotoGallery is a **modern, privacy-first photo management application** built with **Python (Flask) and SQLite**, packaged as a **Windows desktop application**.  
It provides a Google Photos–like experience **entirely offline**, ensuring full control over your photos with **no cloud, no tracking, and no external services**.

The app runs locally on Windows 10/11 and opens in the browser while behaving like a native desktop app.

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

### 🖥️ Desktop-Ready (Windows)
- Packaged as a single `.exe`
- No Python required for end users
- Fully offline
- Portable & fast

---

## 🧰 Technology Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python (Flask) |
| Database | SQLite (hardened connection layer) |
| Frontend | HTML, CSS, JavaScript |
| UI Icons | Google Material Icons |
| Packaging | PyInstaller |
| Storage | Local filesystem |

---

## 🔒 Privacy & Ethics

PhotoGallery is built with privacy as a core principle:

- No cloud uploads
- No analytics or telemetry
- No face recognition storage
- No biometric data retention
- All processing happens locally on your device

---

## 📂 Project Structure

