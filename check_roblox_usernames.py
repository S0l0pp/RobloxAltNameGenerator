import random
import string
import requests
import time

# === sigma reals ===
BASE = "ALT"                # Prefix for usernames
LENGTH = 10                 # Total username length
COUNT = 30                  # Number of usernames to generate
DELAY = 0.5                 # Delay between checks (seconds)
EXPORT = True               # Export available usernames to file
OUTPUT_FILE = "available_usernames.txt"  # Output filename
ROBLOX_API_TIMEOUT = 10     # API request timeout in seconds

# === real ===
def generate_usernames():
    chars = string.ascii_lowercase + string.digits
    return [
        BASE + ''.join(random.choice(chars) for _ in range(LENGTH - len(BASE)))
        for _ in range(COUNT)
    ]

def check_username(name):
    url = f"https://auth.roblox.com/v1/usernames/validate?username={name}&birthday=2000-01-01"
    try:
        response = requests.get(url, timeout=ROBLOX_API_TIMEOUT)
        return response.json().get("message") == "Username is valid"
    except Exception as e:
        print(f"[ERROR] {name}: {e}")
        return False

def main():
    usernames = generate_usernames()
    available = []
    
    print(f"Checking {len(usernames)} usernames...\n")
    
    for name in usernames:
        if check_username(name):
            print(f"AVAILABLE: {name}")
            available.append(name)
        else:
            print(f"TAKEN:     {name}")
        time.sleep(DELAY)
    
    print(f"\nDone. Found {len(available)} available usernames.")
    
    if EXPORT and available:
        with open(OUTPUT_FILE, "w") as f:
            f.write("\n".join(available))
        print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
