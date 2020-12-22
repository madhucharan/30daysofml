def list_operations(num_list):
    sorted_list = num_list.sort()
    even_list=list()
    odd_list=list()
    # final_lists=list()
    for item in sorted_list:
        if item%2==0:
            even_list.append(item)
            sorted_list.pop(item)
        else:
            odd_list.append(item)
            sorted_list.pop(item)
    final_lists= even_list.extend(odd_list).copy()
    print("max : ", max(num_list))
    print("min : ", min(num_list))
    print("final even and odd number lists : ", final_lists)
    del(sorted_list)
        
def main():
    num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    list_operations(num_list)
        
if __name__ == "__main__":
    main()