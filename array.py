
arr = [10,20,30,40,50]

print arr[0] # prints 10
print arr[3] # prints 40
print len(arr) # prints 5 because there are five elements in the array

arr.pop(0) # removes 10 from the list
del arr[0]
print arr[0]

arr.append(80)
arr.append(100)

print arr
