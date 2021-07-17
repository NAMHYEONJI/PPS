#엄청 고민했음... 결국 못해서 찾아봄,,,

from collections import deque

n =int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
