import sys

fileName = input("What file do you want to open? ")
sys.stdin = open(fileName, "r")

multiLine = False
for line in sys.stdin.readlines():
    if multiLine:
        for i in range(len(line) - 1):
            # handle multiline comments with a boolean flag
            if line[i:i+1] == '*/':
                multiLine = False
                break

            sys.stdout.write(line[i])
        sys.stdout.write('\n')
        continue

    for i in range(len(line) - 1):
        # check if a single line comment starts, "//"
        if line[i:i+1] == '//':
            sys.stdout.write(line[i+2:] + "\n")
            break

        # check if a multiline comment starts, "/*"
        if line[i:i+1] == '/*':
            sys.stdout.write(line[i+2:] + "\n")
            multiLine = True
            break
