with open("notes.txt", "a") as f:
  f.write("Today i am studying File I/O and string manipulation in python.")

#open and read the file after the appending:
with open("notes.txt") as f:
  print(f.read())
  


f = open("myfile.txt", "x")

