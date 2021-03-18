r=eval(input('Enter number of rows'))
for i in range(1,r+1):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch+=1
    print()
    