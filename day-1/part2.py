entries = list(open('./day-1/input-ex.txt','r').read().split('\n'))
new_entries = []

sum = 0
for entry in entries:
    num = []
    for i,c in enumerate(entry):
        if c.isdigit():
            num.append(c)
        for d, val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if entry[i:].startswith(val):
                num.append(str(d+1))
                break

    # test = [i for i in entry if i.isdigit()]
    # print(int(test[0] + test[-1]))
    sum += int(num[0] + num[-1])

print(sum)