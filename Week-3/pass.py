print('Hello!')
while True:
    print('What is your name?')
    name = input()
    if name != 'Irina':
        print('Well this cannot go on. I am waiting on somebody else.')
        continue
    if name == 'Irina':
        print('Hi Irina! I missed you. Time to write your password!')
        password = input()
        if password == 'clowncheck':
            print('Access Granted')
            break
        else:
            print('Access Denied')
            num_tries = 1
            while num_tries < 3:
                print('You have ' + str(3-num_tries) + ' tries left. Try again.')
                num_tries = num_tries + 1
                print('What is your password?')
                password = input()
                if password == 'clowncheck':
                    print('Finally')
                    print('Access Granted')
                    break
                else:
                    continue
            if num_tries == 3:
                print('Access denied until you dig around your memory.')
            break