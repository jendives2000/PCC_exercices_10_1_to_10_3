# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Reading files.
# -----------------------------------------------------------------------------
# 2a. Read in each line from the file you just created, learning_python.txt,
# 2a.1a and replace the word Python with the name of another language, such as C.
# 2b. Print each modified line to the screen.
# -----------------------------------------------------------------------------
from pathlib import Path

# -----------------------------------------------------------------------------
path = Path("learning_python.txt")
contents = path.read_text()  # 2a.

lines = contents.splitlines()
contents_string = ""
for line in lines:
    contents_string += line + "\n\n"

replaced_contents = contents_string.replace("Python", "R")  # 2a.1a
print(replaced_contents)  # 2b.
