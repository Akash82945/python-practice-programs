def merge_two_sorted_list(my_list1, my_list2):
    
    i = 0
    j = 0
    
    merge_list = []
    
    while i < len(my_list1) and j < len(my_list2):
        if my_list1[i] <= my_list2[j]:
            merge_list.append(my_list1[i])
            i += 1
            
        else:
            merge_list.append(my_list2[j])
            j += 1
            
    merge_list = merge_list + my_list1[i:]
    
    merge_list = merge_list + my_list2[j:]
            
    return merge_list



my_list1 = input("Enter Values of list1 seperable by space: ")
my_list2 = input("Enter values of list2 seperabe by space: ")

new_list1 = [int(x) for x in my_list1.split()]
new_list2 = [int(y) for y in my_list2.split()]

result = merge_two_sorted_list(new_list1,new_list2)
print(result)