base = int(input("Enter the base of the number: "))
if base > 8 or base < 2:
    print("Error: Invalid base. Only bases between 2 and 8 are allowed.")
else:
    tol = 1
    power = 0
    resault = 0
    decimal = str(input("Enter the decimal number: "))
    for i in decimal:
        if int(decimal[len(decimal)-tol]) > base:
           print("invalid number")
           break
        else:
         int(decimal[len(decimal)-tol]) == 0 
         resault += int(decimal[len(decimal)-tol])*base**(power)
         tol += 1
        power +=1
    print(f"number {decimal} in base {base} is",resault)
    convback = ""
while resault > 0:
  convback = str(resault % base) + convback
  resault = resault // base  
print(f"Converted back to base {base}: {convback}")
 
if decimal == convback:
    print("bravo") 

  
 
 