
str = input()

for i in range(len(str)):
    if str[i] =='A' or str[i] =='B' or str[i] =='C':
        print(chr(ord(str[i])+23), end="")
    else:
        print(chr(ord(str[i])-3), end="")
