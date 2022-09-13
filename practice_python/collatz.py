def collatz(number): 
    '''A function named collatz() that has one parameter named number. 
    If number is even, then collatz() should print number // 2 and return this value. 
    If number is odd, then collatz() should print and return 3 * number + 1
    '''
    if (number % 2 == 0):
        return number // 2
    elif (number % 2== 1):
        return  3 * number + 1      
try:
    print(collatz(int(input("Enter any number: "))))
except ValueError:
    print("Wrong value")
        