#Multiples Part 1, Printing odd numbers in a range
for count in range(1, 1000):
    if(count%2 !=0):
        print(count)
#Multiples Part 2, printing multiples of 5 in a range
for count in range(5, 1000000, 5):
    print(count)
#Sum List, print sum of all values in list
a = [1,2,5,10,255,3]
sum = 0
for count in range(len(a)):
    sum = a[count] + sum
print sum
#Average List, print average of values in list
b = [1,2,5,10,255,3]
sum = 0
avg = 0
for count in range(len(b)):
    sum = a[count] + sum
avg = sum/len(b)
print avg
    