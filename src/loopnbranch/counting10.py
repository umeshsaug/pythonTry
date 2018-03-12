# Python 3

count = 1
# Code block 1
while count:
    if count % 3 == 0:
        continue
    print(count)
    count = count + 1
    print("Count % 3", count%3)
    if count > 10:
        break
# Code block 2
if count == 11:
    print('Counting complete.')
