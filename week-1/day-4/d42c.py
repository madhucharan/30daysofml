def isprime(num):
    if num > 1:    
        # Iterate from 2 to n / 2
        for i in range(2, num):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                
            else:
                return True
        else:
            return True
 

def check_number(num):
    if (isprime(num) and num %2==0):
        print("the number is even prime")
    elif (isprime(num) and not num%2==0):
        print("the number is prime but not even")