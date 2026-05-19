with open("notes.txt", "w") as f:
  f.write("Today i am studying File I/O and string manipulation in python.")

#open and read the file after the overwriting:
with open("notes.txt") as f:
  print(f.read())