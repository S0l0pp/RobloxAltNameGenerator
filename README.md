# RobloxAltNameGenerator
It creates 30 alt names and check if they are taken or not (if names are banned like slurs they result in taken) and saves the one that are free on a file
Remember that in the export section of the code you need to change the directory on wich the file available_usernames.exe is (You need to create it)

if EXPORT:
        if available:
            with open("YOUR available_usernames.exe DIRECTORY", "w", encoding="utf-8") as f:
                f.write("\n".join(available))
        print("📁 Saved to available_usernames.txt")
    else:
        print("⚠️ No available usernames to save.")
