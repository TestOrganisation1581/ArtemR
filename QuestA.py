f=open('input.txt')
a=list(int(x) for x in f)
f.close()
q=-1000000000000000
for i in range(len(a)):
    if a[i]>q and a[i]%100==17:
        q=a[i]
for i in range(len(a)-2):
    if