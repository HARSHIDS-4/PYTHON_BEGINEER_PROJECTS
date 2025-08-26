import pandas as pd

class SALES:
    def __init__(self):
        self.file=pd.read_csv("C:\\Users\\hp\\Downloads\\sales.csv")

    def print_rows(self):
        first=self.file.head(10)
        return first
    
    def missing_values(self):
        missing=self.file.isnull().sum()
        return missing
    
    def sum(self):
        total=0
        total=total+self.file['Total Sale Amount'].sum()
        return total
    
    def average(self):
        total=0
        total=total+self.file['Total Sale Amount'].sum()
        avg=total/len(self.file)
        return avg
    
    def maximum(self):
        max_sale=self.file["Total Sale Amount"].max()
        return max_sale
    
    def top_salers(self):
        top=self.file.sort_values(by=['Total Sale Amount'],ascending=False).head()
        return top[['Salesperson','Total Sale Amount']]

    def top_products(self):
        product=self.file.sort_values(by=['Quantity'],ascending=False).head(1)
        return product[['Product','Quantity']]
    
    def group_data(self):
        group=self.file.groupby('Region')['Total Sale Amount'].sum()
        return group
    
    #method 1
    def mean_std(self):
        mean=self.file['Total Sale Amount'].mean()
        std=self.file['Total Sale Amount'].std()
        for total_sale in self.file['Total Sale Amount']:
            if total_sale>(mean+3*std):
                print(total_sale,"greater")
            else:
                print(total_sale,'lesser')
        return mean,std
    
    #method 2
    def mean_std(self):
        mean=self.file['Total Sale Amount'].mean()
        std=self.file['Total Sale Amount'].std()
        self.file['outliers']=self.file['Total Sale Amount'].apply(lambda x:"greater" if x>(mean+3*std) else "lesser")
        return self.file[['Total Sale Amount','outliers']]
    
    def export_csv(self,path='C:\\Users\\hp\\Downloads\\sales_stored_data.csv'):
        self.file.to_csv(path,index=False)
        return f"file saved to {path}"
    
sales=SALES()
print("FIRST 10 ROWS ARE:")
print(sales.print_rows())
print()
print("THE NUMBER OF NAN VALUES ARE:")
print(sales.missing_values())
print()
print("SUM OF SALES IS:")
print(sales.sum())
print()
print("AVERAGE OF SALES IS:")
print(sales.average())
print()
print("MAXIMUN SALE:")
print(sales.maximum())
print()
print("TOP SALERS ARE:")
print(sales.top_salers())
print()
print("TOP PRODUCTS ARE:")
print(sales.top_products())
print()
print("DATA GROUPED ACCORDING TO REGION BY TOTAL SALE AMOUNT IS:")
print(sales.group_data())
print()
print("mean and standard deviation of sales product are:")
print(sales.mean_std())
print()
print(sales.export_csv())