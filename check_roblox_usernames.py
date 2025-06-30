import random
import string
import requests
import time
import threading
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# === Username generator ===
def gen_usernames(base="", length=8, count=10):
    chars = string.ascii_lowercase + string.digits
    names = []
    for _ in range(count):
        suffix = ''.join(random.choice(chars) for _ in range(length - len(base)))
        names.append(base + suffix)
    return names

# === Username availability checker ===
def check_username(name):
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2000-01-01"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get("message") == "Username is valid"
    except Exception as e:
        return f"[ERROR] {name}: {e}"

# === Main Function ===
def run_check(base, length, count, delay, export, output_box):
    usernames = gen_usernames(base, length, count)
    available = []

    output_box.insert(tk.END, f"☁️ Checking {len(usernames)} usernames...\n\n")
    output_box.update()

    for name in usernames:
        result = check_username(name)
        if result is True:
            output_box.insert(tk.END, f"✅ AVAILABLE: {name}\n")
            available.append(name)
        elif result is False:
            output_box.insert(tk.END, f"❌ TAKEN:     {name}\n")
        else:
            output_box.insert(tk.END, f"{result}\n")
        output_box.update()
        time.sleep(delay)

    output_box.insert(tk.END, f"\n✅ {len(available)} available usernames found.\n")
    if export and available:
        with open("YOUR available_usernames.txt DIRECTORY", "w", encoding="utf-8") as f:
            f.write("\n".join(available))
        output_box.insert(tk.END, "📁 Saved to available_usernames.txt\n")
    elif not available:
        output_box.insert(tk.END, "⚠️ No available usernames to save.\n")

# === GUI Setup ===
def start_gui():
    def on_run():
        try:
            base = base_entry.get()
            length = int(length_entry.get())
            count = int(count_entry.get())
            delay = float(delay_entry.get())
            export = export_var.get()

            if len(base) >= length:
                messagebox.showerror("Input Error", "Base length must be less than total length.")
                return

            output_box.delete(1.0, tk.END)
            threading.Thread(target=run_check, args=(base, length, count, delay, export, output_box), daemon=True).start()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    window = tk.Tk()
    window.title("☁️ Roblox Username Checker")
    window.geometry("700x600")
    window.configure(bg="#e6f2ff")  # Cloudy pastel blue
    window.resizable(False, False)

    font_style = ("Segoe UI", 12)

    # Inputs
    def label(text, row):
        tk.Label(window, text=text, bg="#e6f2ff", font=font_style).grid(row=row, column=0, sticky="e", padx=10, pady=5)

    def entry(default, row):
        e = tk.Entry(window, font=font_style, bg="white", fg="#333", relief="flat", bd=4)
        e.insert(0, default)
        e.grid(row=row, column=1, sticky="w", padx=5, pady=5, ipadx=10, ipady=4)
        return e

    label("Base:", 0)
    base_entry = entry("ALT", 0)

    label("Length:", 1)
    length_entry = entry("10", 1)

    label("Count:", 2)
    count_entry = entry("30", 2)

    label("Delay (s):", 3)
    delay_entry = entry("0.5", 3)

    export_var = tk.BooleanVar(value=True)
    export_check = tk.Checkbutton(window, text="☁ Export available usernames", variable=export_var,
                                  font=font_style, bg="#e6f2ff", activebackground="#e6f2ff")
    export_check.grid(row=4, column=1, sticky="w", padx=5)

    run_button = tk.Button(window, text="☁ Run Check", command=on_run,
                           font=("Segoe UI", 13, "bold"), bg="#b3d9ff", fg="#003366",
                           activebackground="#99ccff", relief="flat", padx=10, pady=8)
    run_button.grid(row=5, column=1, pady=10, sticky="w")

    # Output box
    output_box = scrolledtext.ScrolledText(window, width=80, height=20,
                                           font=("Consolas", 11), bg="white", fg="#333",
                                           relief="flat", bd=5)
    output_box.grid(row=6, column=0, columnspan=2, padx=20, pady=15)

    window.mainloop()

if __name__ == "__main__":
    start_gui()
