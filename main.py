# This script creates a backup of all files in a specified directory.
# Created in Perplexity on 30-10-2023. Woks fine

import os
import shutil
import time

# source = 'D:/Tally Prime/Data'
# destination = 'G:/My Drive/AutoBackup'

source = "C:\\Users\\emeer\\Downloads\\Documents"
destination = "C:\\Transit"

# Define exclusion list
exclusions = ["EPIM", ".txt"]

# Create a new directory with date and time stamp
timestamp = time.strftime("%d-%m-%y _ %H-%M-%S")
new_folder = destination + "/" + timestamp
os.mkdir(new_folder)

# Copy files from source to destination, excluding items in the exclusion list
for root, dirs, files in os.walk(source):
    for exclusion in exclusions:
        if exclusion in dirs:
            dirs.remove(exclusion)
    for file in files:
        if not any(file.endswith(exclusion) for exclusion in exclusions):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(new_folder, os.path.relpath(src_file, source))
            dst_dir = os.path.dirname(dst_file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            shutil.copy2(src_file, dst_file)

# Keep the latest 3 directories and delete the older ones
dirs = sorted(os.listdir(destination), reverse=True)
for dir in dirs[5:]:
    shutil.rmtree(os.path.join(destination, dir))

# Print backup done message
print("Backup done successfully!")
