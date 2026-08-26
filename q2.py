def process_list(list1):
    list2 = list1.copy()
    # for i in range(0, len(list2)):
        # if list2[i]<0:
        #     list2.pop(i)          gives an error because the list size changes during iteration


    for i in range(len(list2)-1,-1,-1):  #backward iteration avoids index errors as the index of forward element doesn't change when we remove an element from the end
        if list2[i]<0:
                list2.pop(i)
    list2.append(0)
    list2.sort()
    return list2

n = int(input("enter the number of elements: "))
list1 = []
for i in range(n):
    elem = int(input("enter list element: "))
    list1.append(elem)

result = process_list(list1)
print("Original: ", list1)
print("Processed: ", result)
