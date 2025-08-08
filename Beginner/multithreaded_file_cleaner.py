""""
An example using threads to delete .tmp and .log files from a folder

It assumes the following things:
1) A folder exists somewhere with .log and .tmp files

To run:
1) python3 multithreaded_file_cleaner.py
2) Enter in folder's path (the folder where the files are stored) -> files will be deleted
"""

import threading
import os

# Create a function that deletes the file
def file_remove(path,files):
    for item in files:
        os.remove(path+"/"+item)

# Get the folder's name (Write the full extension)
folder_path = input("Enter the folder's path? ")
list_of_files = os.listdir(folder_path)

# This part separates the .log and the .tmp files
log_list = []
tmp_list = []
for file_item in list_of_files:
    if file_item.endswith(".log"):
        log_list.append(file_item)
    else:
        tmp_list.append(file_item)

# Define the threads.
log_thread = threading.Thread(target=file_remove, args=(folder_path, log_list,))
tmp_thread = threading.Thread(target=file_remove, args=(folder_path, tmp_list,))
log_thread.start()
tmp_thread.start()

# Makes the calling thread, main thread, wait until 
# the joined threads are complete before it completes its execution.
log_thread.join()
tmp_thread.join()






