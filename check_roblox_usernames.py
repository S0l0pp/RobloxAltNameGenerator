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

    output_box.insert(tk.END, f"Checking {len(usernames)} usernames...\n\n")
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
    window.title("Roblox Username Checker")
    window.geometry("600x500")

    # Inputs
    tk.Label(window, text="Base:").grid(row=0, column=0, sticky="e")
    base_entry = tk.Entry(window)
    base_entry.insert(0, "ALT")
    base_entry.grid(row=0, column=1)

    tk.Label(window, text="Length:").grid(row=1, column=0, sticky="e")
    length_entry = tk.Entry(window)
    length_entry.insert(0, "10")
    length_entry.grid(row=1, column=1)

    tk.Label(window, text="Count:").grid(row=2, column=0, sticky="e")
    count_entry = tk.Entry(window)
    count_entry.insert(0, "30")
    count_entry.grid(row=2, column=1)

    tk.Label(window, text="Delay (s):").grid(row=3, column=0, sticky="e")
    delay_entry = tk.Entry(window)
    delay_entry.insert(0, "0.5")
    delay_entry.grid(row=3, column=1)

    export_var = tk.BooleanVar(value=True)
    export_check = tk.Checkbutton(window, text="Export available usernames", variable=export_var)
    export_check.grid(row=4, column=1, sticky="w")

    run_button = tk.Button(window, text="Run Check", command=on_run)
    run_button.grid(row=5, column=1, pady=10)

    # Output box
    output_box = scrolledtext.ScrolledText(window, width=70, height=20)
    output_box.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    start_gui()
