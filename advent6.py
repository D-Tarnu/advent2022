f = open('advent.txt','r')
text = f.read()

def differ(s):
    for char in s:
        if s.count(char) != 1:
            return False
    return True

for i in range(13,len(text)):
    if differ(text[i-13:i+1]):
        print(i+1)
        break

f.close()
