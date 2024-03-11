# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Reading files.
# -----------------------------------------------------------------------------
# 1a. Open a blank file in your text editor and write a few lines summarizing what you’ve learned about
# Python so far. Start each line with the phrase Python is. . . .
# Save the file as learning_python.txt in the same directory as your exercises from this chapter.
# 1b. Write a program that reads the file
# 1b1. and prints what you wrote two times: print the contents once by reading in the entire file,
# 1b.2. and once by storing the lines in a list and then looping over each line.
# -----------------------------------------------------------------------------
from pathlib import Path

# -----------------------------------------------------------------------------
path = Path("learning_python.txt")  # 1b.
contents = path.read_text()
print(contents)  # 1b1.
lines = contents.splitlines()  # 1b.2.
contents_string = ""
for line in lines:
    contents_string += line + "\n\n"
print(contents_string)
