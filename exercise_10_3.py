# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Reading files.
# -----------------------------------------------------------------------------
# 3a. skip the temporary variable
# 3b. and loop directly over the list that splitlines() returns
# -----------------------------------------------------------------------------
from pathlib import Path

# -----------------------------------------------------------------------------
path = Path("learning_python.txt")
contents = path.read_text()
# 3a. skip the temporary variable
# lines = contents.splitlines()

contents_string = ""
for line in contents.splitlines():  # 3b.
    contents_string += line + "\n\n"

replaced_contents = contents_string.replace("Python", "R")
print(replaced_contents.strip())
