# Desktop Organizer

A Python script to automatically organize and declutter your desktop by categorizing files into specific folders based on their file type.

## Features

- **File Categorization**: Automatically sorts files (e.g., pictures, documents, audio, videos, etc.) into folders like `Pictures`, `Documents`, `Audio`, and more.
- **Shortcut Exclusion**: Skips shortcuts and alias files during the organization process.
- **Customizable Categories**: Supports defining new categories for specific file types.

## How It Works

1. The script scans your desktop for files.
2. Files are moved into a main folder called `Desktop Organizer`, with subfolders for each category.
3. Any file that doesn't match a predefined category is moved to a folder named `Mischievous`.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python to run the script.

## How to Use

1. Download or clone this script to your system.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following command:

   ```bash
   python desktop_cleaner.py
   ```

4. Once completed, a folder named `Desktop Organizer` will be created on your desktop containing all the organized files.

## Default Categories

The following file types are sorted into specific categories:

- **Pictures**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.ppt`, `.pptx`, `.xls`
- **Codes**: `.html`, `.css`, `.js`, `.py`, `.java`, `.cpp`, `.c`, `.php`, `.rb`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`

Files that don't match any category are placed in the `Mischievous` folder.

## Customization

You can edit the `categories` dictionary in the script to add or modify file types and their corresponding folders.

## Notes

- This script works across Windows, macOS, and Linux.
- Shortcuts and aliases (e.g., `.lnk`, `.url`, `.desktop`) are ignored during the cleanup.

## License

This project is open-source and available under the MIT License.

