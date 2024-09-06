# Code to write my own user defined function
#This function will take user input to findout wether user is human or robot
print("Please enter num 1")
num_1 = int(input())
print("Please enter num 2. num 2 should be same as num 1")
num_2 = int(input())

print ("num_1 + num_2 is", num_1 + num_2)
def is_human(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
    
Verified = is_human(num_1, num_2)
if Verified == True:
    print("You are Human!")
else:
    print("You are Robot!")