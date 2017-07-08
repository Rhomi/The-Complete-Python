def main():

    def find_divisors(num):
        print('The divisors of {} are {}'.format(num,[item for item in range(1,num) if num%item == 0]))

    num = int(input('Enter the number you want to find divisors for : '))

    if num != None:
        find_divisors(num)

if __name__ == "__main__":
    main()