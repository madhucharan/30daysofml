try:
    with open('test.txt', 'r') as f:
        # content = f.read()
        # print(content)
        for line in f:
            print(line,end='')
except FileNotFoundError:
    print("File doesn't exist")

    
