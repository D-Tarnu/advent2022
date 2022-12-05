f = open('advent.txt','r')
text = f.read()
text = text.split('\n')
text = [item.split(' ') for item in text]

def cycle(number, iter):
    for i in range(iter):
        number = (number % 3) + 1
    return number

score = 0

points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

for game in text:
    if game[0] == 'A':
        my_points = cycle(points[game[1]],2)
    elif game[0] == 'B':
        my_points = points[game[1]]
    elif game[0] == 'C':
        my_points = cycle(points[game[1]],1)

    if game[1] == 'Y':
        score += 3
    if game[1] == 'Z':
        score += 6

    score += my_points

print(score)

f.close()
