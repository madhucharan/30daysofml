
import d42a
import d42b
import d42c

def main():
    print("square of 4 is :", d42a.square(4))
    num_list = [1, 2, 3, 4, 5, 6, 7]
    print("maximum number in the list is", d42a.max_list(num_list))
    print("minimum number in the list is", d42a.min_list(num_list))
    print("Sum of the numbers in the list is", d42a.sum_list(num_list))
    string= 'my name is madhu charan'
    print("middle character of the string is", d42b.middle(string))
    print("no of vowels in the string is", d42b.vowels_count(string))
    print("no of words in the string is", d42b.word_count(string))
    print("the number 6 is ", d42c.check_number(6))

if __name__ == "__main__":
    main()

