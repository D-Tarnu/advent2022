f = open('advent.txt','r')
text = f.read()
text = text.split('\n')

max_cals = [0,0,0]
current_cals = 0


for line in text:
    if len(line) > 0:
        current_cals += int(line)
    else:
        if current_cals > max_cals[0]:
            max_cals[2] = max_cals[1]
            max_cals[1] = max_cals[0]
            max_cals[0] = current_cals
        elif current_cals > max_cals[1]:
            max_cals[2] = max_cals[1]
            max_cals[1] = current_cals
        elif current_cals > max_cals[2]:
            max_cals[2] = current_cals
        current_cals = 0

print(max_cals[0])
print(max_cals[1])
print(max_cals[2])
print(max_cals[0] + max_cals[1] + max_cals[2])


f.close()
