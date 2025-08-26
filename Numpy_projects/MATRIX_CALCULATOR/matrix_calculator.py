#MATRIX CALCULATOR

import numpy as np

def inputs(rows1,columns1,rows2,columns2):
    matrix1=np.zeros((rows1,columns1))
    matrix2=np.zeros((rows2,columns2))
    print("enter the values")
    for i in range(0,rows1):
        for j in range(0,columns1):
            while True:
                try:
                    value1=int(input(f"MATRIX1[{i}][{j}]:"))
                    matrix1[i][j]=value1
                    break
                except ValueError:
                    print("enter integer value")

    print()
    for h in range(0,rows2):
        for k in range(0,columns2):
            while True:
                try:
                    value2=int(input(f"MATRIX2[{h}][{k}]:"))
                    matrix2[h][k]=value2
                    break
                except ValueError:
                    print("enter integer value")
    return matrix1,matrix2

    
def main():
    while True:
        try:
            r1=int(input("enter the number of rows for matrix 1:"))
            c1=int(input("enter the number of columns for matrix 1:"))
            r2=int(input("enter the number of rows for matrix 2:"))
            c2=int(input("enter the number of columns for matrix 2:"))
            if r1<0 or c1<0 or c2<0 or r2<0:
                print("rows ansd columns can not be negative!")
                continue
            break  
        except ValueError:
            print("value entered is not an integer")
    
    matrix1,matrix2=inputs(r1,c1,r2,c2)
    print("choose the operation you wanted to perform:")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.TRANSPOSE")
    print("5.DOT PRODUCT")
    choice=int(input("enter you choice(1,2,3,4,5):"))
    match(choice):
        case 1:
            if r1==r2 and c1==c2:
                print("sum of two matrix's is:")
                print(matrix1+matrix2)
            else:
                print("enter the equal number of rows and columns") 
        case 2:
            if r1==r2 and c1==c2:
                print("difference of two matrix's is:")
                print(matrix1-matrix2)
            else:
                print("enter the equal number of rows and columns")  
        case 3:
            if r1==r2 and c1==c2:
                print("multiplication of two matrix's is:")
                print(matrix1*matrix2)
            elif r1==c2 and r2==c1:
                print("multiplication of two matrix's is:")
                multi=np.matmul(matrix1,matrix2)
                print(multi)
            else:
                print("enter the equal number of rows and columns")
        case 4:
            print("transpose of matrix 1 is:")
            transpose1=np.transpose(matrix1)
            print(transpose1)
            print("transpose of matrix 2 is:")
            transpose2=np.transpose(matrix2)
            print(transpose2)
        case 5:
            if r1==r2 and c1==c2:
                print("dot prouct is:")
                dp=np.dot(matrix1,matrix2)
                print(dp)
            else:
                print("enter the equal number of rows and columns") 
        case _:
            print("enter choice from above given choices")

if __name__=="__main__":
    main()