#student report card system

class Students:
    def __init__(self,name,id,number_subjects):
        self.name=name
        self.id=id
        self.number_subjects=number_subjects
        self.grades=[]
    

    def add_grades(self):
        for i in range(0,self.number_subjects):
            subject=input("enter the subject:")
            marks=int(input("enter the marks"))
            if marks>100 or marks<0:
                print("marks cannot be greater than 100")
                marks=int(input("re-enter the marks"))
            else:
                pass
            self.grades.append({"subject":subject,"marks":marks})
        print("the subject and their marks entered are:")
        i=0
        for grade in self.grades:
            i=i+1
            print(f"{i}:{grade}")


    def avg_grades(self):
        avg=0
        for grade in self.grades:
            avg=avg+grade['marks']/self.number_subjects
        print(f"average grade is:{avg:.2f}")
        return avg


    def report_card(self,avg):
        print(f"report card for {self.name} is (ID:{self.id})")
        for grade in self.grades:
            print(f"{grade['subject']}:{grade['marks']}")
        print(f"average grade:{avg:.2f}")


#user inputs
std_name=input("enter the student name:")
std_id=input("enter the student id:")
while True:
    try:
        n=int(input("enter the number of subjects:"))
        if n<0:
            print("number of subjects can not be negative")
            n=int(input("enter the number of subjects:"))
        else:
            pass
    except ValueError:
        print("value entered is not an integer❌")
        n=int(input("re-enter the number of subjects:"))


#printing details
students=Students(std_name,std_id,n)
print()
students.add_grades()
avg=students.avg_grades()
print()
print('-'*40)
students.report_card(avg)
print('-'*40)