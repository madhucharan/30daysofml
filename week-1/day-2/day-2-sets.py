def set_operations(set1,set2):
    difference_set = set1.difference(set2)
    union_set = set1.union(set2)
    copy_union_set = union_set.copy()
    intersection_set = set1.intersection(set2)
    even_set =set()
    odd_set =set()
    for item in union_set:
        if item%2==0:
            even_set.add(item)
            copy_union_set.remove(item)
        elif item%2==1:
            odd_set.add(item)
            copy_union_set.remove(item)
    print(" union ", union_set)
    print(" even", even_set)
    print(" odd", odd_set)
    print(" intersection ", intersection_set)
    print(" difference ", difference_set)    
    print(" is even_set is a subset of union set ? ", even_set.issubset(union_set))
    print(" is odd_set is a subset of union set ? ", odd_set.issubset(union_set)) 

def main():
    set1={1,2,3,4,5,6,7,8,9,10}
    set2={11,12,13,14,15,16,17,18,19,20}
    set_operations(set1,set2)

if __name__ == "__main__":
    main()       

