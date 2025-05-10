
Keylogger Project
Python
License

A comprehensive keylogger application written in Python that captures keyboard inputs, mouse activities, system information, takes screenshots, and records microphone input, sending the collected data to a specified email address at regular intervals.

Features
Keystroke Logging: Captures all keyboard inputs including special keys

Mouse Activity Tracking: Records mouse movements, clicks, and scrolls

System Information Collection: Gathers hostname, IP address, processor info, and system specs

Screenshot Capture: Takes periodic screenshots of the user's desktop

Audio Recording: Records microphone input at specified intervals

Email Reporting: Sends collected data to a configured email address

Stealth Operation: Includes self-removal capabilities

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/keylogger.git
cd keylogger
Install dependencies:

bash
pip install -r requirements.txt
Or install manually:

bash
pip install pyscreenshot sounddevice pynput
Configuration
Before running the keylogger, you need to configure your email settings:

Open the script in a text editor

Modify these lines with your email credentials:

python
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
SEND_REPORT_EVERY = 10  # Time interval in seconds
For Mailtrap users (default configuration), use:

python
SMTP_SERVER = "smtp.mailtrap.io"
SMTP_PORT = 2525
Usage
Run the keylogger with Python:

bash
python keylogger.py
The program will:

Start capturing keyboard and mouse inputs

Collect system information

Take periodic screenshots and audio recordings

Send reports via email at the specified interval

Security and Legal Considerations
⚠️ Important Notice:

This software is for educational and legitimate monitoring purposes only

Unauthorized monitoring of computers may violate privacy laws

Always obtain proper consent before using this tool

The developer is not responsible for misuse of this software

Technical Details
Components
Keyboard Listener: Uses pynput to capture keystrokes

Mouse Listener: Tracks mouse movements and clicks

Screenshot: Uses pyscreenshot to capture desktop images

Audio Recording: Uses sounddevice to record microphone input

Email Reporting: Uses smtplib for sending collected data
