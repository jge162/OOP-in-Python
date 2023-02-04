import os
import shutil

# Set the path to the Downloads folder
downloads_folder = "/Users/home/Downloads"

# Create a dictionary to map file extensions to subfolder names
extension_map = {
    "pdf": "PDF Files",
    "doc": "Word Files",
    "docx": "Word Files",
    "xls": "Excel Files",
    "xlsx": "Excel Files",
    "ppt": "PowerPoint Files",
    "pptx": "PowerPoint Files",
    "jpg": "Image Files",
    "jpeg": "Image Files",
    "png": "Image Files",
    "gif": "Image Files",
    "mp3": "Audio Files",
    "wav": "Audio Files",
    "mp4": "Video Files",
    "mkv": "Video Files"
}

# Loop through all the files in the Downloads folder
for filename in os.listdir(downloads_folder):
    # Get the file extension
    extension = os.path.splitext(filename)[1][1:].lower()

    # Check if the file extension is in the extension map
    if extension in extension_map:
        # Get the subfolder name from the extension map
        subfolder_name = extension_map[extension]

        # Create the subfolder if it doesn't exist
        subfolder_path = os.path.join(downloads_folder, subfolder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        # Move the file to the subfolder
        file_path = os.path.join(downloads_folder, filename)
        shutil.move(file_path, os.path.join(subfolder_path, filename))

print("Downloads folder organized.")