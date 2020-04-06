print("\n\n***** Reading Files *****\n")

print("\nContent of main file read all at once:\n")
with open('main.py') as mainFile:
  contents = mainFile.read();
print(contents)

print("\n\nContent of dummy file line by line:")
with open('data/dummy_file.txt') as dummyFile:
  for line in dummyFile:
    print(line, end='')

print("\n\nContent of dummy file line by line:")
combined_lines = ''
with open('data/dummy_file.txt') as dummyFile:
  lines = dummyFile.readlines()
  for line in lines:
    combined_lines += line
print(combined_lines)