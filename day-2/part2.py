entries = list(open('./day-2/input-ex.txt','r').read().split('\n'))
ans = 0

for entry in entries:
    red = 0
    green = 0
    blue = 0

    for bag in entry.split(':')[1].strip().split(';'):        
        for item in bag.strip().split(', '):
            amount = int(item.split(' ')[0])
            color = item.split(' ')[1]

            if (color == 'red' and amount > red):
                red = amount
            elif (color == 'blue' and amount > blue):
                blue = amount
            elif (color == 'green' and amount > green):
                green = amount

    ans += red * green * blue

print(ans)
