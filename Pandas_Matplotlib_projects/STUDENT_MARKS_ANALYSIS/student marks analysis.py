import pandas as pd
import matplotlib.pyplot as plt

class STUDENTS:
    def __init__(self):
        self.path=pd.read_csv("C:\\Users\\hp\\Downloads\\student_marks.csv")  
        self.subjects=self.path[['Mathematics','Science','English','History','Computer']]  

    def print_file(self):
        return self.path
    
    def sub_sum(self):
        add=self.subjects.sum()
        return add
    
    def missing(self):
        self.path=self.path.fillna(0)
        return self.path
    
    def total_marks(self):
        self.path['Total Marks']=self.subjects.sum(axis=1)
        return self.path[['Student','Total Marks']]
    
    def average_marks(self):
        self.path['Total Marks']=self.subjects.sum(axis=1)
        self.path['Average Marks']=self.path['Total Marks']/5
        return self.path[['Student','Average Marks']]
    
    
    def subject_status(self):
        conv=self.path.melt(id_vars='Student',value_vars=self.subjects,var_name='Subjects',value_name='Marks')
        conv['Subject Status']=conv['Marks'].apply(lambda x:"pass" if x>33 else "fail")
        final_result=conv.pivot(index='Student',columns=['Subjects'],values=['Marks','Subject Status'])
        return final_result
   
    def GRADES(self):
        self.path['Grade']=self.path['Average Marks'].apply(lambda x:"A" if x>=80 else("B" if x>=60 and x<80 else("C" if x>=40 and x<60 else "FAIL")))
        return self.path
    
    def toppers(self):
        top=self.path.sort_values(by='Average Marks',ascending=False).head()
        return top   

    def sub_avg(self):
        total=self.subjects.sum() 
        average=total/10 
        return average
    
    def hardest_subject(self):
        total=self.subjects.sum() 
        average=total/10 
        hardest=average.idxmin()
        hardest_subject = self.subjects.loc[hardest].idxmin()
        return hardest_subject
    
    def failure_percentage(self,final_result):
        check=final_result['Subject Status']
        failure=(check=="fail").sum()
        fail_percentage=(failure/len(self.path))*100
        return fail_percentage
    
    def bar_chart(self,average):
       fig,ax=plt.subplots(1,2,figsize=(10,5))
       """ax[0].bar(self.subjects,average,color='aqua')
       ax[0].set_title('Subject average marks')
       self.path['Grade']=average.apply(lambda x:"A" if x>=80 else("B" if x>=60 and x<80 else("C" if x>=40 and x<60 else "FAIL")))
       ax[1].pie(self.path['Grade'],labels=self.subjects,autopct="%1.1f%%")
       ax[1].set_title('Grades per subject')
       fig.suptitle("grades and average per subject is:")
       #plt.show()"""
       print(type(self.subjects), self.subjects)
       print(type(average), average)
       print(average.apply(type))


students=STUDENTS()
print(students.print_file())
print()
print("the sum of each subject is:")
print(students.sub_sum())
print()
print("missing values filled with 0")
print(students.missing())
print()
print("total marks are:")
print(students.total_marks())
print()
print("Average marks for students are:")
print(students.average_marks())
print()
print("Subject status is:")
final_result=students.subject_status()
print(final_result)
print()
print("GRADES ARE")
print(students.GRADES())
print()
print("TOPPERS OF BATCH ARE:")
print(students.toppers())
print()
print("Average marks of each subject are:")
average=students.sub_avg()
print(average)
print()
print("bar graph for subject average printed")
print(students.bar_chart(average))
print("hardest subject is:")
print(students.hardest_subject())
print()
print("percentage of failure in each subject is:")
print(students.failure_percentage(final_result))