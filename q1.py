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