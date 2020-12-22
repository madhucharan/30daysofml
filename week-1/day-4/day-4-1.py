def show_prime_matrix(num):
    target = num*num
    count = 0
    i=0
    prime_numbers = []
    while count <target:
        if (isprime(i)):
            prime_numbers.append(i)
            count+=1
        i=i+1
        
    print("length of the list : ",len(prime_numbers))
    counter=0
    for j in range(num):
        for k in range(num):
            print(prime_numbers[counter],end=" ")
            counter+=1
        print("\n")



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


def main():
    num= int(input('enter the matrix size :'))
    show_prime_matrix(num)

if __name__ == "__main__":
    main()       
