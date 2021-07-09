#뒤에 있어서 어려운 문제인줄 알았는데 괜찮았다
n = int(input())
def word_change(idx, x):
    print('String #{}'.format(idx))
    for i in x:
        if i == 'Z':
            print('A', end='')
        else:
            print(chr(ord(i)+1), end='')

for i in range(n):
    word = input()
    word_change(i+1, word)
    print("\n")