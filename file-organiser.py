import os
import shutil
import time

# Set the path to the directory you want to organize
# TIP: Use a raw string (r"...") for Windows paths to avoid issues with backslashes
WATCH_PATH = r"C:\Users\YourUser\Downloads"

# Define the destination folders for different file types
DEST_DIRS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"],
    "Executables": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"]
}

def organize_files(path):
    """
    Sorts files in the given path into subdirectories based on their extension.
    """
    # Get a list of all files in the directory
    # os.scandir() is more efficient than os.listdir()
    with os.scandir(path) as entries:
        for entry in entries:
            # Skip if it's a directory
            if entry.is_dir():
                continue

            file_path = entry.path
            file_name = entry.name
            file_extension = os.path.splitext(file_name)[1].lower() # Get the file extension (e.g., ".pdf")

            # Find a destination directory for this file type
            moved = False
            for dir_name, extensions in DEST_DIRS.items():
                if file_extension in extensions:
                    # Create the destination directory if it doesn't exist
                    dest_path = os.path.join(path, dir_name)
                    os.makedirs(dest_path, exist_ok=True) # exist_ok=True prevents errors if folder exists

                    # Move the file
                    try:
                        shutil.move(file_path, os.path.join(dest_path, file_name))
                        print(f"Moved: {file_name} -> {dir_name}/")
                        moved = True
                        break # Stop checking once moved
                    except Exception as e:
                        print(f"Error moving {file_name}: {e}")
            
            # Move all other files to an "Other" folder
            if not moved:
                dest_path = os.path.join(path, "Other")
                os.makedirs(dest_path, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(dest_path, file_name))
                    print(f"Moved: {file_name} -> Other/")
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")

if __name__ == "__main__":
    print(f"Watching directory: {WATCH_PATH}")
    # You could run this once
    organize_files(WATCH_PATH)
    print("Organization complete.")

    # Or, to run it continuously (like a background service):
    # try:
    #     while True:
    #         organize_files(WATCH_PATH)
    #         time.sleep(10) # Wait 10 seconds before checking again
    # except KeyboardInterrupt:
    #     print("Stopping organizer.")