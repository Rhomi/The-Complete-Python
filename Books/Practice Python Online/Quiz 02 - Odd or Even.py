
# coding: utf-8
def num_checker(number, checker):
    if number%2 == 1:
        print('{} is odd.'.format(number))
    else:
        print('{} is even.'.format(number))
    if number%4 == 0:
        print('{} also happens to be a multiple of 4.'.format(number))
    if number%checker == 0:
        print('And {} divides perfectly into {}.'.format(checker,number))
    else:
        print("But {} doesn't divide {} evenly.".format(checker,number))




