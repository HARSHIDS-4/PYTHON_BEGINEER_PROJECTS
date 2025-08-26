
year=int(input("enter the year:"))
month=int(input("enter the month(1-12)"))
date=int(input("enter the date(1-31):"))

if month in (1,3,5,7,8,10,12):
    if month in (1,3,5,7,8,10) and date==31:
        print(f"1-{month+1}-{year}")
    elif month==12 and date==31:
        print(f"01-01-{year+1}")
    else:
        print(f"{date+1}-{month}:{year}")
        
elif month==2:
    if year%4==0 and date==28 :
        print(f"1-{month+1}-{year}")
    else:
        print(f"{date+1}-{month}-{year}")

elif month in (4,6,9,11) and date==31:
        print(f"1-{month+1}-{year}")

else:
    print(f"{date+1}-{month}-{year}")