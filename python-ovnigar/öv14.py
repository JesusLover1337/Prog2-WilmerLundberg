from sys import stdin

input = []
line = stdin.readline()
while line:                
    input.append(line)
    line = stdin.readline()

line = 0
while line < len(input):
    x=""
    y=[]
    for number in input[line]:
        if number == " ":
            y.append(int(x))
            x=""
        else:
            x = x + number
    y.append(int(x))
    print(abs(y[0]-y[1]))
    line = line + 1

            




