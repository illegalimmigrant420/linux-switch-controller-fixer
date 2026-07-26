#!/usr/bin/env python3
import subprocess
import time
import os
import sys
import tkinter as tk
from tkinter import messagebox

CONTROLLER_1 = "YOUR_FIRST_MAC_HERE"
CONTROLLER_2 = "YOUR_SECOND_MAC_HERE"

def log(msg):
    console.config(state='normal')
    console.insert(tk.END, f"> {msg}\n")
    console.see(tk.END)
    console.config(state='disabled')
    root.update()

def fix_and_launch():
    try:
        log("INITIATING OVERRIDE...")
        log("Bypassing udev permissions...")
        subprocess.run("sudo chmod 0666 /dev/hidraw*", shell=True)

        log("Scanning frequency spectrum (3s)...")
        subprocess.run("bluetoothctl --timeout 3 scan on", shell=True)

        log(f"Jacking into NODE 1 [{CONTROLLER_1}]...")
        subprocess.run(f"bluetoothctl connect {CONTROLLER_1}", shell=True)

        log(f"Jacking into NODE 2 [{CONTROLLER_2}]...")
        subprocess.run(f"bluetoothctl connect {CONTROLLER_2}", shell=True)

        log("Terminating Steam matrix instance...")
        subprocess.run("pkill -9 steam", shell=True)
        time.sleep(2)

        log("Re-initializing Steam mainframe...")
        subprocess.Popen(["steam"])

        log("SYSTEM FULLY OPERATIONAL. ENJOY THE SIMULATION.")
    except Exception as e:
        log(f"ERROR DETECTED: {str(e)}")

# Matrix GUI Setup
root = tk.Tk()
root.title("MATRIX // CONTROLLER OVERRIDE")
root.geometry("420x300")
root.configure(bg="#0d0d0d")

tk.Label(root, text="[ MATRIX CONTROLLER LINK ]", font=("Courier", 14, "bold"), fg="#00ff66", bg="#0d0d0d").pack(pady=10)

console = tk.Text(root, height=8, width=45, bg="#000000", fg="#00ff66", font=("Courier", 9), insertbackground="#00ff66")
console.pack(pady=5)
console.insert(tk.END, "> SYSTEM READY. Press override button below...\n")
console.config(state='disabled')

btn = tk.Button(root, text="[ OVERRIDE & LAUNCH ]", command=fix_and_launch, bg="#00ff66", fg="#000000", font=("Courier", 11, "bold"), activebackground="#00cc55", activeforeground="#000000", bd=0, padx=10, pady=5)
btn.pack(pady=10)

root.mainloop()
