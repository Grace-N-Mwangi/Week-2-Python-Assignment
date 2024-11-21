#Question 1: Create empty list
my_list = []

#Question 2: Append elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Question 3: Insert 15 at 2nd position
my_list.insert(1,15)

#Question 4: Extend list
my_list.extend([50,60,70,80])

#Question 5: Remove last element
my_list.pop()

#Question 6: Sort in ascending order
my_list.sort()

#Question 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 in the list is: {index_of_30}")

# Final list after all operations
print(f"Final list: {my_list}")
