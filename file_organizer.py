import os
import shutil

# Folder to organize
path = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Documents": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xlsx"]
}

# Create folders if not exist
for folder in file_types.keys():
    os.makedirs(os.path.join(path, folder), exist_ok=True)

os.makedirs(os.path.join(path, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    moved = False

    for folder, extensions in file_types.items():

        if file.lower().endswith(tuple(extensions)):

            destination = os.path.join(path, folder, file)

            shutil.move(file_path, destination)

            print(f"Moved: {file} → {folder}")

            moved = True
            break

    if not moved:
        destination = os.path.join(path, "Others", file)

        shutil.move(file_path, destination)

        print(f"Moved: {file} → Others")

print("\nOrganization Complete!")