#STUDENT MARKS ANALYZER

import numpy as np

def input_subjects(number_subjects):
    sub=[]
    print("enter the subjects you want:")
    for j in range(0,number_subjects):
        subjects=input(f"{j+1}.").upper()
        sub.append(subjects)
    return sub    

def input_marks(number_students,number_subjects,sub):
    marks=np.zeros((number_students,number_subjects))
    for i in range(0,number_students):
        print(f"Student {i+1}.")
        for j in range(0,number_subjects):
            while True:
                try:
                    mark=int(input(f"  enter marks for {sub[j]}:"))
                    if  mark<0 or mark>100:
                        print("marks entered are invalid(either negative or greater than 100)")
                        continue
                    else:
                        marks[i][j]=mark
                        break

                except ValueError:
                    print("value entered is not an integer❌")
    return marks


def Statistical_Analysis(marks):
            mean=np.mean(marks,axis=0,)
            median=np.median(marks,axis=0,)
            std=np.std(marks,axis=0,)
            max=np.max(marks,axis=0)
            min=np.min(marks,axis=0)
            avg=np.mean(marks,axis=1)
            print("-------------FOR EACH SUBJECT--------------")
            print(f"mean:                  {mean}")
            print(f"median:                {median}")
            print(f"standard deviation:    {std}")
            print(f"highest marks:         {max}")
            print(f"lowest marks:          {min}")
            print(f"average marks of each student is:{avg}")
            print("--------------------------------------------")


def Data_Manipulation(marks):
     sort=np.sort(marks,axis=0)
     print("sorted marks are:",sort)


def main():
    num_std=int(input("enter the number of students:"))
    num_sub=int(input("enter the number of subjects:"))
    sub= input_subjects(num_sub)
    marks=input_marks(num_std,num_sub,sub)
    print()
    Statistical_Analysis(marks)
    Data_Manipulation(marks)

if __name__=="__main__":
    main()