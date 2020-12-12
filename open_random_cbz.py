import os
import random

'''
Written by GitHub account JamesH117
To turn into executable file,
(1) make sure pyinstaller in installed with command: pip install pyinstaller
(2) Run command in same directory as script file: pyinstaller --onefile <your_script_name>.py
(2a) To customize icon, add before <your_script_name>.py: --icon=<icon_name_here>.ico
'''

cwd = os.getcwd()
items_inside_dir = []

# Get all books in same folder as executable
for f in os.listdir(cwd):
    if f.endswith(".cbz"):
        items_inside_dir.append(os.path.join(cwd,f))

random_book = random.choice(items_inside_dir)
os.startfile(random_book)

# Write to text file what file was opened
with open(os.path.join(cwd, "OpenedBook.txt"), "a") as f:
    f.write("{}\n".format(os.path.splitext(random_book.split('\\')[-1])[0]))
