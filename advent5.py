f = open('advent.txt','r')
text = f.read()
text = text.split('\n')
text = [t.replace('move ', '') for t in text]
text = [t.replace(' from ', ' ') for t in text]
text = [t.replace(' to ', ' ') for t in text]
text = [t.split(' ') for t in text]

crate = ['SCVN','ZMJHNS','MCTGJND','TDFJWRD','PFH','CTZHJ','DPRQFSLZ','CSLHDFPW','DSMPFNGZ']

for t in text:
    t[0] = int(t[0])
    t[1] = int(t[1])
    t[2] = int(t[2])

    l = len(crate[t[1]-1]) - t[0]
    add = crate[t[1]-1][l:]
    
    crate[t[2]-1] += add
    crate[t[1]-1] = crate[t[1]-1][:l]

print(crate)

f.close()
