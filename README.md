# 🛡️ KeyLogger Surveillance Tool (Educational Use Only)

> ⚠️ **DISCLAIMER:**  
> This software is intended **strictly for ethical, educational, or authorized testing purposes** only. Unauthorized deployment or use of keylogging software may be **illegal** in your country and can result in **criminal charges**.  
>  
> You are solely responsible for how you use this tool. Always obtain **explicit consent** before running on any device that is not your own.

---

## 📌 Project Overview

The **KeyLogger Surveillance Tool** is a Python-based script that simulates a basic surveillance system. It is capable of:

- Logging keyboard inputs
- Monitoring clipboard activity
- Taking screenshots
- Recording short microphone audio clips
- Gathering system information
- Packaging and sending all collected data via email (using [Mailtrap](https://mailtrap.io/))

This tool is ideal for learning about:
- Ethical hacking
- Penetration testing
- System monitoring
- Python scripting with system-level interaction

---

## 🧰 Features

| Feature               | Description                                      |
|----------------------|--------------------------------------------------|
| 🧠 Keystroke Logging  | Captures all key presses                         |
| 📋 Clipboard Logger   | Logs copied clipboard text every 5 seconds       |
| 📷 Screenshot Capture | Takes a screenshot at each report interval      |
| 🎤 Microphone Audio   | Records 3-second audio using system microphone   |
| 🖥️ System Info        | Logs system details (CPU, OS, IP, etc.)         |
| 📩 Email Reports      | Sends logs and media via email using SMTP        |
| 🧼 Auto Cleanup       | Deletes files after sending to prevent buildup   |

---

## ✉️ Email Setup Using Mailtrap (Safe for Testing)

Mailtrap lets you **test emails safely** without sending them to a real recipient. Use it to test this tool without risk.

### ✅ Step-by-Step Setup

### 🥇 Step 1: Create a Mailtrap Account

1. Visit [https://mailtrap.io/](https://mailtrap.io/)
2. Sign up for a free account

---

### 🥈 Step 2: Create an Inbox & Copy SMTP Credentials

1. Go to your **Mailtrap dashboard**
2. Click **"Email Testing" > Inbox > SMTP Settings**
3. Choose **"Integrations > Python (smtplib)"**
4. Copy the following:
   - SMTP Host: `smtp.mailtrap.io`
   - Port: `2525`
   - Username
   - Password

---

### 🥉 Step 3: Paste Credentials into the Code

In `keylogger.py`, modify these lines:

```python
EMAIL_ADDRESS = "your_mailtrap_username"
EMAIL_PASSWORD = "your_mailtrap_password"
