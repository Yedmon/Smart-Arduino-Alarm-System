import tkinter as tk
from tkinter import messagebox
from serial_comm import send_command
from config import PASSWORD

def start_gui():
    app = tk.Tk()
    app.title("Smart Arduino Alarm System")
    app.geometry("400x420")

    def log(msg):
        log_box.insert(tk.END, msg + "\n")

    def arm():
        if password_entry.get() == PASSWORD:
            send_command('A')
            status_label.config(text="STATUS: ARMED", fg="red")
            log("System Armed")
        else:
            messagebox.showerror("Access Denied", "Wrong Password")

    def disarm():
        if password_entry.get() == PASSWORD:
            send_command('D')
            status_label.config(text="STATUS: DISARMED", fg="green")
            log("System Disarmed")
        else:
            messagebox.showerror("Access Denied", "Wrong Password")

    def alarm():
        send_command('L')
        status_label.config(text="STATUS: ALARM ACTIVE", fg="red")
        log("ALARM TRIGGERED")

    tk.Label(app, text="Enter Password").pack()
    password_entry = tk.Entry(app, show="*")
    password_entry.pack()

    tk.Button(app, text="ARM SYSTEM", command=arm).pack(pady=5)
    tk.Button(app, text="DISARM SYSTEM", command=disarm).pack(pady=5)
    tk.Button(app, text="TEST ALARM", command=alarm).pack(pady=5)

    status_label = tk.Label(app, text="STATUS: DISARMED", fg="green")
    status_label.pack(pady=10)

    log_box = tk.Text(app, height=10)
    log_box.pack()

    app.mainloop()
