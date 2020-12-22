def show_length(str1,str2):
    return len(str1+str2)

def main():
    str1 = input("enter string1: ")
    str2 = input("enter string2: ")
    print("The length of the string after concatination is : "+str(show_length(str1,str2)))

if __name__ == "__main__":
    main()

