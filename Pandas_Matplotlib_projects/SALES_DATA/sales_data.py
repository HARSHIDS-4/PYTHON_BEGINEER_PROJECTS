import pandas as pd
import matplotlib.pyplot as plt

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
    
    def trends(self):

#filling null values
        self.file['Date']=self.file['Date'].fillna(self.file['Date'].mode()[0])
        self.file['Total Sale Amount']=self.file['Total Sale Amount'].fillna(self.file['Total Sale Amount'].mean())
        self.file[['Minutes','Seconds']]=self.file['Date'].str.split(":",expand=True)
        self.file['Region']=self.file['Region'].fillna(self.file['Region'].mode()[0])

#Sales Trend Over Time
        self.file['Minutes']=pd.to_numeric(self.file['Minutes'])
        trend=self.file.groupby('Minutes')['Total Sale Amount'].sum()
        trend.plot(color='blue',marker='o')
        plt.xlabel("Minutes")
        plt.ylabel("Total Sales")
        plt.title('Sales Trend Over Time')
        plt.grid(linestyle=":",color='Grey')
        plt.show()

#Sales by Region 
        bar_region=self.file.groupby('Region')['Total Sale Amount'].sum()
        bar_region.plot(kind='bar',color='Aqua',label='number of sales')
        plt.xlabel("region")
        plt.ylabel("Sales")
        plt.legend()
        plt.show()

#METHOD 1
        fig,ax=plt.subplots(1,2,figsize=(10,10))
        ax[0].bar(bar_region.index,bar_region.values)
        ax[0].set_title("Sales by Region")
        bar_salesperson=self.file.groupby('Salesperson')['Total Sale Amount'].count().sort_values(ascending=False).head()
        ax[1].bar(bar_salesperson.index,bar_salesperson.values)
        ax[1].set_title("Top 5 Salespersons")
        fig.suptitle("DATA FOR SALES AND SALESPERSON")
        plt.tight_layout()
        plt.show()

#METHOD 2
        fig,ax=plt.subplots(1,2,figsize=(10,5))
        ax[0].pie(bar_region,labels=bar_region.index,autopct="%1.1f%%",shadow=True)
        ax[0].set_title("sales by region")

        ax[1].pie(bar_salesperson,labels=bar_salesperson.index,autopct="%1.1f%%")
        ax[1].set_title("top 5 salesperson")
        fig.suptitle("DATA FOR SALES AND SALESPERSON")
        plt.tight_layout()
        plt.show()

#Most Sold Product 
        product=self.file.groupby('Product')['Total Sale Amount'].sum()
        product.plot(kind="bar")
        plt.xlabel("product")
        plt.ylabel("Sales amount")
        plt.show()
    
    
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
print(sales.trends())