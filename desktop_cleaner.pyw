import os
import shutil

def is_shortcut(file_path):
    """
    Check if a file is a shortcut or alias across platforms, including internet shortcuts.
    """
    file_name = os.path.basename(file_path)
    _, file_extension = os.path.splitext(file_name)

    # For Windows shortcuts
    if file_extension.lower() in [".lnk", ".url"]:
        return True

    # For Linux/Mac shortcuts (e.g., .desktop files)
    if file_extension.lower() == ".desktop":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            # Check if the .desktop file is an internet shortcut
            if "Type=Link" in content or "URL=" in content:
                return True

    # Add other shortcut file types if needed
    return False


def move_files_to_category(source_folder, main_folder, categories):
    """
    Categorizes and moves files from the source folder into specific folders inside the main folder.
    """
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        
        # Skip folders and shortcuts
        if os.path.isdir(source_path) or is_shortcut(source_path):
            continue

        # Determine file extension
        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()

        # Check the category or fallback to 'Mischievous'
        destination_folder = categories.get(file_extension, os.path.join(main_folder, "Mischievous"))
        
        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        # Move the file
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name} -> {destination_folder}")


def main():
    # Desktop folder path
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Main folder to hold all organized files
    main_folder = os.path.join(desktop, "Desktop Organizer")
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    # Define categories and their respective extensions
    categories = {
        # Pictures
        ".jpg": os.path.join(main_folder, "Pictures"),
        ".jpeg": os.path.join(main_folder, "Pictures"),
        ".png": os.path.join(main_folder, "Pictures"),
        ".gif": os.path.join(main_folder, "Pictures"),
        ".bmp": os.path.join(main_folder, "Pictures"),
        ".svg": os.path.join(main_folder, "Pictures"),
        ".webp": os.path.join(main_folder, "Pictures"),

        # Documents
        ".pdf": os.path.join(main_folder, "Documents"),
        ".docx": os.path.join(main_folder, "Documents"),
        ".doc": os.path.join(main_folder, "Documents"),
        ".txt": os.path.join(main_folder, "Documents"),
        ".xlsx": os.path.join(main_folder, "Documents"),
        ".pptx": os.path.join(main_folder, "Documents"),
        ".ppt": os.path.join(main_folder, "Documents"),
        ".xls": os.path.join(main_folder, "Documents"),

        # Codes
        ".html": os.path.join(main_folder, "Codes"),
        ".css": os.path.join(main_folder, "Codes"),
        ".js": os.path.join(main_folder, "Codes"),
        ".py": os.path.join(main_folder, "Codes"),
        ".java": os.path.join(main_folder, "Codes"),
        ".cpp": os.path.join(main_folder, "Codes"),
        ".c": os.path.join(main_folder, "Codes"),
        ".php": os.path.join(main_folder, "Codes"),
        ".rb": os.path.join(main_folder, "Codes"),

        # Audio
        ".mp3": os.path.join(main_folder, "Audio"),
        ".wav": os.path.join(main_folder, "Audio"),
        ".aac": os.path.join(main_folder, "Audio"),
        ".flac": os.path.join(main_folder, "Audio"),

        # Videos
        ".mp4": os.path.join(main_folder, "Videos"),
        ".mov": os.path.join(main_folder, "Videos"),
        ".avi": os.path.join(main_folder, "Videos"),
        ".mkv": os.path.join(main_folder, "Videos"),
        ".flv": os.path.join(main_folder, "Videos"),
    }

    # Move files to categorized folders inside the main folder
    move_files_to_category(desktop, main_folder, categories)

    print("Desktop cleanup completed! All files are now organized inside 'Desktop Organizer'.")


if __name__ == "__main__":
    main()
