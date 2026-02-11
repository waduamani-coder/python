Grossincome=float(input("enter gross income  "))
if Grossincome < 0 :
    print("invalid input")
elif Grossincome <= 5999 :
    print("Your monthly contribution is ksh 150.00") 
elif Grossincome >6000 and Grossincome<7999:
    print("Your monthly contribution is ksh300.00")       
elif Grossincome >=8000 and Grossincome<11999 :
    print("Your monthly contribution is ksh400.00")       
elif Grossincome >=12000 and Grossincome<14999:
    print("Your monthly contribution is ksh500.00")       
elif Grossincome >=15000 and Grossincome<19999: 
    print("Your monthly contribution is ksh600.00")       
elif Grossincome >=20000 and Grossincome<24999:
    print("Your monthly contribution is ksh750.00")       
elif Grossincome >=25000 and Grossincome<29999:
    print("Your monthly contribution is ksh850.00")       
elif Grossincome >=30000 and Grossincome<49999:
    print("Your monthly contribution is ksh1000.00")       
elif Grossincome >=50000 and Grossincome<99999:
    print("Your monthly contribution is ksh1500.00")       
elif Grossincome >100000 :
    print("Your monthly contribution is ksh2000.00")       
else: print("invalid")

