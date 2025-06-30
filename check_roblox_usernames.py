import random
import string
import requests
import time

# === SETTINGS ===
BASE = "ALT"         # Prefix for usernames
LENGTH = 10          # Total username length
COUNT = 30           # Number of usernames to generate
DELAY = 0.5          # Delay between checks (seconds, avoid rate limit)
EXPORT = True        # Export available usernames to a file

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
        print(f"[ERROR] {name}: {e}")
        return False

# === Main ===
def main():
    usernames = gen_usernames(BASE, LENGTH, COUNT)
    available = []

    print(f"Checking {len(usernames)} usernames...\n")
    for name in usernames:
        valid = check_username(name)
        if valid:
            print(f"✅ AVAILABLE: {name}")
            available.append(name)
        else:
            print(f"❌ TAKEN:     {name}")
        time.sleep(DELAY)

    print("\nDone.")
    print(f"\n✅ {len(available)} available usernames found.")
    if EXPORT:
        if available:
            with open("YOUR available_usernames.exe DIRECTORY", "w", encoding="utf-8") as f:
                f.write("\n".join(available))
        print("📁 Saved to available_usernames.txt")
    else:
        print("⚠️ No available usernames to save.")


if __name__ == "__main__":
    main()
