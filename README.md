# 📂 Automated File Organizer

A simple yet powerful Python automation project that automatically organizes files into categorized folders based on their file extensions. This project helps keep directories clean and improves file management by sorting files into predefined folders.

---

## 🚀 Features

- 📁 Automatically organizes files into categorized folders
- 🖼️ Supports Images, PDFs, Videos, Music, and Documents
- 📂 Creates folders automatically if they do not already exist
- 📦 Moves unsupported file types into an **Others** folder
- ⚡ Fast, lightweight, and easy to use
- 🐍 Beginner-friendly Python automation project

---

## 🛠️ Technologies Used

- **Python 3**
- **os** module
- **shutil** module

---

## 📁 Project Structure

```
Automated_File_Organizer/
│
├── file_organizer.py
├── README.md
└── sample_files/          (Optional)
```

---

## 📋 Supported File Categories

| Category | Supported Extensions |
|----------|----------------------|
| 🖼️ Images | .jpg, .jpeg, .png, .gif, .bmp |
| 📄 PDFs | .pdf |
| 🎥 Videos | .mp4, .mkv, .avi, .mov |
| 🎵 Music | .mp3, .wav |
| 📑 Documents | .doc, .docx, .txt, .ppt, .pptx, .xlsx |
| 📦 Others | Any unsupported file extension |

---

## ⚙️ How It Works

1. The user enters the path of the folder to organize.
2. The program scans all files in the selected folder.
3. It identifies each file based on its extension.
4. Required folders are created automatically if they do not exist.
5. Files are moved into their respective category folders.
6. Unknown file types are placed inside the **Others** folder.

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Automated-File-Organizer.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Automated-File-Organizer
```

### Step 3: Run the Program

```bash
python file_organizer.py
```

### Step 4: Enter Folder Path

Example:

```text
Enter folder path:
C:\Users\YourName\Downloads
```

---

## 📸 Example Output

```text
Moved: photo.jpg → Images
Moved: song.mp3 → Music
Moved: notes.pdf → PDFs
Moved: movie.mp4 → Videos
Moved: project.docx → Documents
Moved: random.xyz → Others

Organization Complete!
```

---

## 📂 Before Organization

```text
Downloads/
│
├── photo.jpg
├── song.mp3
├── notes.pdf
├── movie.mp4
├── project.docx
└── random.xyz
```

---

## 📂 After Organization

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Music/
│   └── song.mp3
│
├── PDFs/
│   └── notes.pdf
│
├── Videos/
│   └── movie.mp4
│
├── Documents/
│   └── project.docx
│
└── Others/
    └── random.xyz
```

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- Python file handling
- Working with directories and folders
- File automation using Python
- Using the **os** module
- Using the **shutil** module
- Conditional statements and loops
- Organizing files efficiently

---

## 💡 Future Improvements

- Add a graphical user interface (GUI)
- Automatically monitor folders in real time
- Support custom file categories
- Add logging functionality
- Undo file organization feature
- Cross-platform compatibility improvements

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Submit a Pull Request.

---

## 📜 License

This project is created for educational and learning purposes. Feel free to use and modify it according to your needs.

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub. It motivates me to build more automation and Python projects!

---
