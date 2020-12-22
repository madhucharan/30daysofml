import sys
# userInput = sys.stdin.readlines()
line= str(input("Enter the lines "))
lines = line.split("\n")
try:
    f = open("test.txt", "a")
    f.writelines(lines)
except FileNotFoundError:
    print("File doesn't exist")
else:
    f.close()
