def display(fullName,collegeDetail,marks):
    '''input the name , college details and marks as a list and print them including the total sum and percentage'''
    print("My name is "+fullName)
    print("College Detail are "+collegeDetail)
    print("Total Marks are "+str(sum(marks))+"/500")
    print("total percentage is "+str((sum(marks)/500)*100))

def main():
    ''' Enters each and every details from print statements and stores it in variables and calls the display function by passing the arguments'''
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    fullName = firstName + " " + lastName
    collegeDetail = input("EntercollegeDetail: ")
    englishMarks = eval(input("Enter English marks: "))
    mathMarks = eval(input("Enter math marks: "))
    scienceMarks = eval(input("Enter science marks: "))
    chemistryMarks = eval(input("Enter chemistry marks: "))
    labMarks = eval(input("Enter lab marks: "))
    marks= [englishMarks,mathMarks,scienceMarks,chemistryMarks,labMarks]
    display(fullName,collegeDetail,marks)



if __name__ == "__main__":
    main()