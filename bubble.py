a = []

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if int(a[i]) >int(a[j]) :
            a[i],a[j] = a[j],a[i]
print(a)

