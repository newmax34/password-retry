
i = 3
password = 'a123456'
while i > 0: 
    answer = input ('please enter password: ')
    if password == answer: 
        print('Correct. Now you can access.')
        break
    else:
        i = i - 1
        print ('Incorrect! You have', i, 'chance(s)')

