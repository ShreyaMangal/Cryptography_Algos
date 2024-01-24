# Reads numbers repeatedly till the users enters "done". Once "done" is entered print total, count, and average. 
# Use try and except if the user enters anything other than numbers. Skip the mistake.

total = 0
count = 0
while True: # No need to assign a flag value to variable value. We can just run while loop infinitely till the user enters done and then break out of the loop.
    value = input("Enter a number: ")
    if value == 'done':
        break
    try :
        num = float(value)
    except :
        '''if value == "done" : # instead of dealing with done in except we can deal with it before try. Good Practise
            break'''
        print("Please enter numeric values only!")
        continue
    total = total + num
    count = count + 1
average = total / count
print("Count:",count)
print("Total:",total)
print("Average:",average)