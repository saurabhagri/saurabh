import os
import subprocess
import time
import tkinter as tk
from tkinter import filedialog
def select_file():
   root = tk.Tk()
   root.withdraw()  # Hide the main window
   file_path = filedialog.askopenfilename()  # Open file dialog to select a file
   root.destroy()
   return file_path
def update_repository():
   # Navigate to the repository directory
   # repo_path = 'https://github.com/akshaypophale/1307'
   repo_path = 'https://github.com/saurabhagri/saurabh.git'
   # Prompt the user to select a file
   text_file_path = select_file()
   # Check if the file exists
   if os.path.exists(text_file_path):
       # Change directory to the repository
       os.chdir('D:\\GM\\Demo\\saurabh\\')
       # Add the file to the repository
       subprocess.run(["git", "add", "."])
       # Commit the changes
       subprocess.run(["git", "commit", "-m", "text file found"])
       # Push the changes to the remote repository
       subprocess.run(["git", "push"])
   else:
       print("Text file does not exist or no file selected. Please select a file and try again.")
# Run the update function initially
update_repository()
# Schedule the update to occur every 24 hours
while True:
   # Sleep for 24 hours
   time.sleep(24*60*60)
   # Update the repository
   update_repository()