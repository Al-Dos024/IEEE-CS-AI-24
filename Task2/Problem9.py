input_set1 = input("Enter Set 1 elements separated by spaces: ")
elements1 = input_set1.split()
set1 = set(elements1)

input_set2 = input("Enter Set 2 elements separated by spaces: ")
elements2 = input_set2.split()
set2 = set(elements2)

common_elements = set1.intersection(set2)
print("Common elements:", common_elements)



