
i = 3
password = 'a123456'
while True: 
    answer = input ('please enter password: ')
    if password == answer: 
        print('Correct. Now you can access.')
        break
    else:
        i = i - 1
        print ('Incorrect! You have', i, 'chance(s)')
        if i == 0:
            break
