entries = list(open('./day-2/input-ex.txt','r').read().split('\n'))
game_ids = []
not_correct_game_ids = []

for entry in entries:
    game_index = int(entry.split(' ')[1].split(':')[0])
    game_ids.append(game_index)

    for bag in entry.split(':')[1].strip().split(';'):        
        for item in bag.strip().split(', '):
            amount = int(item.split(' ')[0])
            color = item.split(' ')[1]

            if (color == 'red' and amount > 12):
                not_correct_game_ids.append(game_index)
            elif (color == 'blue' and amount > 14):
                not_correct_game_ids.append(game_index)
            elif (color == 'green' and amount > 13):
                not_correct_game_ids.append(game_index)

res = [i for i in game_ids if i not in not_correct_game_ids]
print(sum(res))