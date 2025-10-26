# 📧 PyMail Automator

**PyMail Automator** is an advanced **Email Automation System** built entirely with **Python**.  
It can send personalized, templated, and scheduled emails in bulk with attachments, logging, and a simple GUI.

---

## 🚀 Features
- Send emails with or without attachments
- Use `.env` for secure credential storage
- Dynamic HTML templates with **Jinja2**
- Recipient data management via **CSV**
- Detailed logging system
- Schedule emails using **Schedule**
- Simple and elegant **Tkinter GUI**
- Optional enhancements like retry, history tracking, and progress bar

---

## 🧩 Tech Stack
- **Language:** Python
- **Libraries:** smtplib, ssl, pandas, dotenv, jinja2, schedule, tkinter, logging, csv, os, mimetypes, time
- **IDE:** Visual Studio Code

---

## 📂 Folder Structure

core/ → Backend logic
gui/ → Tkinter GUI
templates/ → HTML email templates
data/ → CSV and sent history
logs/ → Log files
docs/ → Documentation files

---

## 🛠️ Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/PyMail-Automator.git
   cd PyMail-Automator

2. Install dependencies:
    pip install -r requirements.txt

3. Set up your .env file: