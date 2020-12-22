import math

def calc_circle_area(radius):
    return math.floor(math.pi * math.pow(radius, 2))

def main():
    radius= eval(input("Enter radius :"))
    print("The area of circle with radius "+str(radius)+" is "+str(calc_circle_area(radius)))
    # calc_circle_area(radius)

if __name__ == "__main__":
    main()
 
