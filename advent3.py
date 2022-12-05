f = open('advent.txt','r')
text = f.read()
text = text.split('\n')

itemsum =  0

for i in range(int(len(text)/3)):
    pair = ''

    for item in text[3*i]:
        if pair.find(item) == -1 and text[3*i+1].find(item) != -1:
            pair += item
    for item in pair:
        if text[3*i+2].find(item) != -1:
            if item.islower():
                itemsum += ord(item)-96
            else:
                itemsum += ord(item)-38
            break

print(itemsum)

f.close()
