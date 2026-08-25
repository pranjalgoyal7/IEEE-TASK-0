n= int(input("enter the number of elements: "))
list1 = []
for i in range(0,n):
    l = int(input("enter element:  "))
    list1.append(l)

# largest element
max_element = list1[0]
for i in range(0,n):
    if list1[i] > max_element:
        max_element = list1[i]
print("largest element is: ", max_element)

#smallest element
min_element = list1[0]
for i in range(0,n):
    if list1[i] < min_element:
        min_element = list1[i]
print("smallest element is: ", min_element)

#sum of elements
sum = 0
for i in range(0,n):
    sum += list1[i]

print("sum of elements is: ",sum)

#number of even elements
even_count = 0
for i in range(0,n):
    if list1[i] % 2 == 0:
        even_count += 1
print("number of even elements is: ",even_count)

#number of odd elements
odd_count = 0
for i in range(0,n):
    if list1[i] % 2 != 0:
        odd_count += 1
print("number of odd elements is: ",odd_count)

#reverse of the list
rev_list = []
for i in range(n-1,-1,-1):
    rev_list.append(list1[i])
print("reverse of the list is: ",rev_list)