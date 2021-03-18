r = eval(input('Enter number of rows '))
ch = 65
for i in range(1, r + 1):
    for j in range(1, i + 1):
        print(chr(ch), end=' ')
        ch += 1
    print()
