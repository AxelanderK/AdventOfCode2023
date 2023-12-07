entries = list(open('./day-1/input-ex.txt','r').read().split('\n'))

sum = 0
for entry in entries:
    test = [i for i in entry if i.isdigit()]
    sum += int(test[0] + test[-1])

print(sum)