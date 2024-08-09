a = []

while True: 
        print('\nadd - adding value.')
        print('q - recive shorted value.')

        user_input= input()

        if user_input == 'add':
            element = input('Entar a value. ')
            a.append(element)

        if user_input == 'q':
             break

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if int(a[i]) >int(a[j]) :
            a[i],a[j] = a[j],a[i]
print(a)

