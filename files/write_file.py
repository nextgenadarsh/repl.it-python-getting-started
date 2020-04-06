print("\n\n***** Writing to Files *****\n")


print("\n\n\nWriting to new file 'dummy_file_new.txt': ")

with open('data/dummy_file_new.txt', 'w') as dummyFile:
  dummyFile.write('\nThis first line is written using Python code.')
  dummyFile.write(' This second line is also written using Python code.')

print("Appending to existing file 'dummy_file_new.txt': ")

with open('data/dummy_file_new.txt', 'a') as dummyFile:
  dummyFile.write('\nThis third line is appended using Python code.')
  dummyFile.write(' This fourth line is also appended using Python code')

print("Reading existing file 'dummy_file_new.txt': ")

with open('data/dummy_file_new.txt') as dummyFile:
  for line in dummyFile:
    print(line, end='')