#Only a single value
print('Hello',sep=' ')
print('Hello',end=' * ')
print('Hello',sep=' ',end='\n**')

#Counts as a single value
a = [1,2,3,4] # A list
print(a)
print(a,sep=' * ')

#Trying to print multiple values at the same time. Can see the use of separator
a = 1
b = 2
c = 3
print(a,b,c)
print(a, b, c,sep =' ** ')


arr = [2,3,6,6,5]
x = list(arr)
x_new = sorted(x)

# [i for i in x_new if i < max(x_new)] --> creates a list of all the elements less than max element in x_new
# So basically you have a new list and then you are printing the last element in the new list
print([i for i in x_new if i < max(x_new)][-1])