from tqdm import tqdm
import os
import shutil
import traceback

def copyAllPackets():
    # Prompt the user to enter the source and destination folders
    source_folder = input("Enter the path to the source folder: ")
    destination_folder = input("Enter the path to the destination folder: ")

    # Get a list of all files in the source directory and its subdirectories
    all_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Filter the list of files to include only files with the .zip or .html extensions
    files = [file for file in all_files if file.endswith(".zip") or file.endswith(".html")]

    # Loop through all files and copy them to the destination directory
    for file in tqdm(files):
        source_path = file
        destination_path = os.path.join(destination_folder, os.path.basename(file))
        shutil.copy(source_path, destination_path)

    # Prompt the user to press any key before exiting
    print(f"[!] Transfer complete: {destination_folder}")
    input("Press any key to exit...")

choice = str(input("""\n
====================NOTICE======================
THIS IS A TOOL FOR COPYING PACKETS IN ONE SHOT.
(File types: .html & .zip)

INTENDED FOR SPECIFIC-USE ONLY.
(Such as: Source province's data packets)
====================NOTICE======================

Choose an option: 
        Y Start
        N Exit
Choice: """))
if choice.lower() == 'y':
    copyAllPackets()
elif choice.lower() == 'n':
    quit()
else:
    traceback.print_exc()
    input("Press any key to exit...")