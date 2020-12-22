def middle(string):
    length=len(string)
    return string[length//2]

def vowels_count(string):
    length=len(string)
    vowel=['a','e','i','o','u']
    count=0
    for i in range(0, length):
        if string[i] in vowel:
            count+=1
    return count

def word_count(string):
    word_list=string.split(' ')
    return len(word_list)


