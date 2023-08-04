num_of_star = int(input('請輸入列印行數: '))

for i in range(num_of_star):
    for i in range(i+1):
        print('*',end='')
    i +=1
    print('\n',end='')

for i in range(num_of_star):
    for i in range(num_of_star):
        print('*',end='')
    num_of_star -=1
    print('\n',end='')

