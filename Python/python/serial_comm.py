import serial
import time
import threading
from tkinter import messagebox
from config import PORT, BAUDRATE

arduino = serial.Serial(PORT, BAUDRATE)
time.sleep(2)

def send_command(cmd):
    def worker():
        try:
            arduino.write(cmd.encode())
        except:
            messagebox.showerror("Error", "Failed to send command to Arduino")

    threading.Thread(target=worker, daemon=True).start()
