def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    def list_less_than_num(list, num):
        print('The resulting list is {}'.format([item for item in a if item<num]))
        
    num = int(input('Enter an arbitrary number : '))
    if num != None:
        list_less_than_num(a, num)
        
if __name__ == "__main__":
    main()