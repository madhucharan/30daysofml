def show_fullname(firstName,lastName):
    return firstName + " " + lastName

def show_total(marks):
    return sum(marks)

def show_percent(marks):
    total = show_total(marks)
    return total/len(marks)

def show_grade(marks):
    i=0
    for mark in marks:
        i+=1
        if mark>=95:
            print("grade in subject "+str(i) + ": A")
        elif mark>=85 and mark<95:
            print("grade in subject "+str(i) + ": B")
        elif mark>=75 and mark<85:
            print("grade in subject "+str(i) + ": C")
        elif mark>=65 and mark<75:
            print("grade in subject "+str(i) + ": D")
        else:
            print("grade in subject "+str(i) + ": E")

def main():
    firstName = input("Please input first name: ")
    lastName = input("Please input last name: ")
    marks = []
    for i in range(5):
        print(" Enter subject "+str(i+1) + " marks : ")
        mark = eval(input ())
        marks.append(mark)
        
    print(" Name : ",show_fullname(firstName,lastName))
    print(" total marks : ",show_total(marks))
    print(" total percentage : ",show_percent(marks))
    print(" Grades in each subject : ",show_grade(marks))

if __name__ == "__main__":
    main()
