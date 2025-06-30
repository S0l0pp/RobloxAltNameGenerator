# RobloxAltNameGenerator
Creates how many alt names you want and checks if they are taken or not, the ones that are taken will not be saved in the file, when you to a new run the txt file will automaticlly delete the old ones and save the new ones so that you don't need to worry about space problems.

if EXPORT:
        if available:
            with open("YOUR available_usernames.exe DIRECTORY", "w", encoding="utf-8") as f:
                f.write("\n".join(available))
        print("📁 Saved to available_usernames.txt")
    else:
        print("⚠️ No available usernames to save.")
