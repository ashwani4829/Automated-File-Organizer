First project intership

📂 Automated File Organizer
A simple Python automation project that automatically organizes files into categorized folders based on their file extensions.

🚀 Features
Automatically sorts files into folders
Supports Images, PDFs, Videos, Music, and Documents
Creates folders automatically if they don't exist
Moves unknown file types to an "Others" folder
Beginner-friendly Python project
🛠️ Technologies Used
Python 3
os module
shutil module
📁 Project Structure
Automated_File_Organizer
│
├── file_organizer.py
└── README.md
📋 Supported Categories
Category	Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp
PDFs	.pdf
Videos	.mp4, .mkv, .avi, .mov
Music	.mp3, .wav
Documents	.doc, .docx, .txt, .ppt, .pptx, .xlsx
▶️ How to Run
Clone the repository
git clone https://github.com/yourusername/Automated-File-Organizer.git
Navigate to the project folder
cd Automated-File-Organizer
Run the program
python file_organizer.py
Enter the folder path you want to organize
Example:

Enter folder path:
C:\Users\Ali\Downloads
📸 Example Output
Moved: photo.jpg → Images
Moved: song.mp3 → Music
Moved: notes.pdf → PDFs
Moved: movie.mp4 → Videos
Moved: project.docx → Documents
Moved: random.xyz → Others

Organization Complete!
Before Organization
Downloads
│
├── photo.jpg
├── song.mp3
├── notes.pdf
├── movie.mp4
├── project.docx
└── random.xyz
After Organization
Downloads
│
├── Images
│   └── photo.jpg
│
├── Music
│   └── song.mp3
│
├── PDFs
│   └── notes.pdf
│
├── Videos
│   └── movie.mp4
│
├── Documents
│   └── project.docx
│
└── Others
    └── random.xyz
🎯 Learning Outcomes
File handling in Python
Working with directories
Automation using Python
Using os and shutil modules
Conditional logic and loops
