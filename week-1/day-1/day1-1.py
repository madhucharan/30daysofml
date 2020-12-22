def oper(num1,num2):
    '''prints the four basic math operations'''
    print("sum : ",num1+num2)
    print("difference : ",num1-num2)
    print("multiplier : ",num1*num2)
    print("division : ",num1/num2)

def main(): 
    ''' main function'''
    num1 = int(input("enter number 1 : "))
    num2 = int(input("enter number 2 : "))
    oper(num1,num2)
if __name__ == "__main__":
    main()