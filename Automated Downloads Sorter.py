import os
import shutil
from pathlib import Path

# Define the directory where downloads are located
downloads_folder = Path(r"C:\Users\jerom\Downloads") 

# Define folders based on file extensions
extension_folders = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.txt': 'Text',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.xlsx': 'Spreadsheets',
    '.pptx': 'Presentations',
    '.mp3': 'Audio',
    '.flac':'Audio',
    '.mp4': 'Videos',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.7zip': 'Archives',
    '.exe': 'Executables',
    '.msi': 'Executables',
    '.csv': 'Spreadsheets',
    '.html': 'Webpages',
    '.json': 'Data',
    '.xml': 'Data',
}

# Create folders if they don't exist
def create_folder(folder_name):
    folder_path = downloads_folder / folder_name
    if not folder_path.exists():
        folder_path.mkdir()
    return folder_path

# Sort files by extension
def sort_files():
    for file in downloads_folder.iterdir():
        if file.is_file():  # Only process files, not directories
            file_extension = file.suffix.lower()  # Get file extension and make it lowercase
            
            if file_extension in extension_folders:
                # Get the destination folder
                folder_name = extension_folders[file_extension]
                destination_folder = create_folder(folder_name)
                
                # Move the file to the corresponding folder
                destination_path = destination_folder / file.name
                print(f"Moving file {file.name} to {destination_path}")
                shutil.move(str(file), str(destination_path))

# Run the sorting function
if __name__ == '__main__':
    sort_files()
    print("Files have been sorted.")
