name_one = input("Type in the name of the first character: ")

try:
    num_one = int(input("Type in the power level of the first character: "))
except:
    print("Invalid input, restarting program.")
    
name_two = input("Type in the name of the second character: ")

try:
    num_two = int(input("Type in the power level of the second character: "))
except:
    print("Invalid input, restarting program.")
        
num_result = num_one / num_two
num_result_two = num_two / num_one

def num_res():
    if num_one > num_two:
        print(name_one + " is", num_result ,"times", "stronger than " + name_two)
    elif num_two > num_one:
        print(name_two + " is" , num_result_two ,"times", "stronger than " + name_one)
        return(num_result_two)
        

print(num_res())

def num_alt():
    if num_result or num_result_two >= 1.25:
        return("(-Start to dominate-)")
    elif num_result or num_result_two >= 1.5:
        return("(-Easy to overwhelm-)")
    elif num_result or num_result_two >= 1.75:
        return("(-High end domination-)")
    elif num_result or num_result_two >= 2.00:
        return("(-Tank attacks unhurt-)")
    elif num_result or num_result_two >= 2.25:
        return("(-Raw power manipulation-)")

print(num_alt())