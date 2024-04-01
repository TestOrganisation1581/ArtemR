f=open('input.txt')
a=list(int(x) for x in f)
f.close()
q=-1000000000000000
for i in range(len(a)):
    if a[i]>q and a[i]%100==17:
        q=a[i]
w=0
e=-10000000000000000
for i in range(len(a)-2):
    if (a[i]+a[i+1]+a[i+2])>q and ((len(str(a[i]))==4 and len(str(a[i+1]))==4 and len(str(a[i+2]))!=4) or (len(str(a[i]))==4 and len(str(a[i+1]))!=4 and len(str(a[i+2]))==4) or (len(str(a[i]))!=4 and len(str(a[i+1]))==4 and len(str(a[i+2]))==4)) and  (a[i]%5==0 or a[i+1]%5==0 or a[i+2]%5==0):
        w=w+1
        if (a[i]+a[i+1]+a[i+2])>e:
            e=a[i]+a[i+1]+a[i+2]
print(w,e)