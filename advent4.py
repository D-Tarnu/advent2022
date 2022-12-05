f = open('advent.txt','r')
text = f.read()
text = text.split('\n')
text = [line.split(',') for line in text]

counter = 0

def compare(a,b,c):
    return a <= b and b <= c

def overlap(sched):
    if compare(sched[0][0],sched[1][0],sched[0][1]) or compare(sched[0][0],sched[1][1],sched[0][1]):
        return True
    elif compare(sched[1][0],sched[0][0],sched[1][1]) or compare(sched[1][0],sched[0][1],sched[1][1]):
        return True
    else:
        return False

for line in text:
    sched = [s.split('-') for s in line]
    sched = [[int(x) for x in y] for y in sched]
    
    if overlap(sched):
        counter += 1

print(counter)

f.close()
