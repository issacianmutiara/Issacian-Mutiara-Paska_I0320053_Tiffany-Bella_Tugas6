
for x in range(10,25) :
    if x == 1:
        print(x, 'bukan prima')
    elif x == 2:
        print(x, 'adalah bilangan prima')
    else:
        for i in range(2,x):
            if x % i == 0:
                print(x, 'bukan prima')
                break
        else:
            print(x, 'adalah bilangan prima')

