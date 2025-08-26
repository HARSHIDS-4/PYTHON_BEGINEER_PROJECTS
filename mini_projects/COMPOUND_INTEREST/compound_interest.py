import math
P=float(input("enter the principal value"))

while P<=0:
    print("principle cannot be less than or equal to zero.")
    P=float(input("enter the principle value:"))
print(f"principle value is:{P}")


R=float(input("enter the interest rate(in percentage):"))

while R<=0:
    print("interest rate can not be less than or equal to zero.")
    R=float(input("enter the interest rate(in percentage):"))
print(f"the interest rate is:{R}")


T=float(input("enter the time period(in days):"))

while T<=0:
    print("time period can not be negative or zero:")
    T=float(input("enter the time period(in days):"))
print(f"the value of time period entered is:{T}")

A=P * pow((1+R/100),T)
print(f"the final amount is:{A}")