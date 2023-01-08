try:
    power_level = int(input("Stronger characters power level: "))
    power_level_2 = int(input("Weaker characters power level: "))
except:
    print("Invalid input, use integers.")
    
result = power_level / power_level_2

def power():
    if result >= 2.25:
        return result
    elif result >= 2:
        return result 
    elif result >= 1.75:
        return result 
    elif result >= 1.5:
        return result 
    elif result >= 1.25:
        return result 
    elif result < 1.25:
        return result 

def power_info():
    if result >= 2.25:
        return "(-Raw power manipulation-)"
    elif result >= 2:
        return "(-Tank attacks unhurt-)"
    elif result >= 1.75:
        return "(-High end domination-)"
    elif result >= 1.5:
        return "(-Easy to overwhelm-)"
    elif result >= 1.25:
        return "(-Start to overwhelm-)"
    elif result < 1.25:
        return "(-Equal in power-)"
        

print(power())
print(power_info())
