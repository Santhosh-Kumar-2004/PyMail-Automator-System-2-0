### **6️⃣ docs/Phase_Structure.md**
A clear, detailed reference of all 12 phases (with the optional features added):

```markdown
# 🧱 PyMail Automator - Project Phases

This document describes the complete 12-phase roadmap of **PyMail Automator**, including mandatory and optional features.

---

## **Phase 1: Basic Email Sending**
- Use `smtplib` and `ssl` to send a basic email.
- Add plain-text and HTML support.

---

## **Phase 2: Email with Attachments**
- Implement file attachments using `mimetypes`.
- Support multiple attachment formats.

---

## **Phase 3: Using Environment Variables**
- Store credentials (email, password) in `.env` file.
- Use `dotenv` for secure loading.

---

## **Phase 4: Logging System**
- Add logging for all actions (info & error).
- Store logs in `/logs/` with daily rotation.

---

## **Phase 5: Reading Recipients from CSV**
- Load recipients and names from `recipients.csv`.
- Add email validation using regex.

---

## **Phase 6: CSV Reader Enhancement**
- Use `pandas` for efficient data processing.
- Allow editing recipient info before sending.

---

## **Phase 7: Sending Emails in Loop**
- Iterate over CSV and send personalized emails.
- Add time delay between sends.

---

## **Phase 8: Personalizing Email Body**
- Add placeholders like `{{ name }}` for personalization.
- Replace dynamically using CSV data.

---

## **Phase 9: Optional Attachments Logic**
- Add optional attachments per recipient.
- Create checkbox/flag later in GUI.

---

## **Phase 10: HTML Templates with Jinja2**
- Build dynamic templates using Jinja2.
- Store in `/templates/` folder.
- Add preview feature before sending (optional).

---

## **Phase 11: Error Handling**
- Implement robust try/except logic.
- Log all errors with timestamps.

---

## **Phase 12: GUI Development**
- Build a Tkinter GUI with:
  - Subject & body input
  - CSV file selector
  - Send/start/stop buttons
  - Progress bar & status display
- Integrate all backend features.

---

## 💎 Optional Enhancements
- ✅ Email preview popup before send
- ✅ Scheduler (send later)
- ✅ Retry mechanism for failed emails
- ✅ Save sent email history
- ✅ GUI progress bar
- ✅ Detailed logging

---

## 🏁 Completion Goal
**Phase 12 marks project completion**, with a fully functional, GUI-driven, production-ready Email Automation System.