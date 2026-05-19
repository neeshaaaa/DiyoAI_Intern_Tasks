f = open("notes.txt")
print(f.read())



with open("notes.txt", "r") as file:
    content = file.read()
print(content)



f = open("notes.txt")
print(f.readline())
f.close()



with open("notes.txt") as f:
  for x in f:
    print(x)
    