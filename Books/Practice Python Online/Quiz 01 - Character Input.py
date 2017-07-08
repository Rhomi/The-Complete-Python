
# coding: utf-8

import time
def main():
    now = time.gmtime()
	name = input('Enter your name :')
    age = input('Enter your age :')
    count = int(input('How many times would you like to see the same message on your screen?'))
    for i in range(count+1):
        print("Hello {}!! You are {} years young :). You will be 100 years young by {}.\n".
              format(name,age,now.tm_year+(100-27)))
if __name__ == "__main__":
    main()

