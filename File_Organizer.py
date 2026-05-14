import os
import shutil

# Change these paths to your own folders
SOURCE = "your/source/folder/path"
DESTINATION = "your/destination/folder/path"

# File types
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    if not os.path.exists(DESTINATION):
        os.makedirs(DESTINATION)

    for filename in os.listdir(SOURCE):
        file_path = os.path.join(SOURCE, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(DESTINATION, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"✅ {filename} → {folder}")
                    moved = True
                    break

if __name__ == "__main__":
    organize_files()
