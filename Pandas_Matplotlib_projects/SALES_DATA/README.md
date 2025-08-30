# 📊 Sales Data Analysis (Python, Pandas & Matplotlib)

This project is a **Sales Data Analysis tool** built in Python using **Pandas** and **Matplotlib**.  
It performs **data cleaning, statistical analysis, and visualization** on sales records to extract useful business insights.

---

## 🚀 Features

- Load sales data from CSV  
- View the **first 10 rows** of the dataset  
- Detect and handle **missing values**  
- Calculate:  
  - Total Sales Amount  
  - Average Sales Amount  
  - Maximum Sale Value  
- Identify:  
  - Top Salespersons  
  - Most Sold Products  
- Group data by **Region** to analyze regional sales  
- Detect **outliers** using mean & standard deviation  
- Export cleaned data back to CSV  
- Generate visualizations:
  - Sales trend over time  
  - Sales by region (bar chart & pie chart)  
  - Top 5 Salespersons (bar chart & pie chart)  
  - Most sold product (bar chart)  

---

## 📦 Requirements

- Python 3.x  
- pandas  
- matplotlib  

## Install dependencies:
```bash
pip install pandas matplotlib
```

---

## 💻 How to Run

1. Place your dataset sales.csv in the specified directory (C:\Users\hp\Downloads\ or update the path in code).

2. Run the script:
    ```bash
    python sales_analysis.py
    ```

3. the program will print statistics in the console and display multiple charts.

4. Cleaned data will be exported to:
    ```bash
    C:\Users\hp\Downloads\sales_stored_data.csv
    ```

---

## 📝 Example Output
```
FIRST 10 ROWS ARE:
   Order ID     Date Region Salesperson   Product  Quantity  Unit Price  Total Sale Amount
0    1001.0  00:00.0  North         Eva  Keyboard       7.0       740.0             5180.0
1    1002.0  53:58.2   West       David   Monitor       4.0       878.0             3512.0
2    1003.0  47:56.4  North       Alice    Laptop       8.0       572.0             4576.0
3    1004.0  41:54.6   West         Eva    Laptop       5.0       250.0             1250.0
4    1005.0  35:52.8   West       Alice     Phone       7.0       514.0             3598.0
5    1006.0  29:51.0   West     Charlie       NaN       3.0       397.0             1191.0
6    1007.0  23:49.1  North       Alice     Phone       7.0       710.0             4970.0
7    1008.0  17:47.3   East       Alice     Phone       8.0       362.0             2896.0
8    1009.0  11:45.5   West       Alice     Phone       5.0       863.0             4315.0
9    1010.0  05:43.7  South       David    Tablet       4.0       243.0              972.0

THE NUMBER OF NAN VALUES ARE:
Order ID             2
Date                 1
Region               4
Salesperson          3
Product              3
Quantity             4
Unit Price           5
Total Sale Amount    3
dtype: int64

SUM OF SALES IS:
542550.0

AVERAGE OF SALES IS:
2712.75

MAXIMUN SALE:
8028.0

TOP SALERS ARE:
    Salesperson  Total Sale Amount
131       David             8028.0
138       David             8019.0
49        Alice             7960.0
73        David             7856.0
173     Charlie             7856.0

TOP PRODUCTS ARE:
   Product  Quantity
61  Laptop       9.0

DATA GROUPED ACCORDING TO REGION BY TOTAL SALE AMOUNT IS:
Region
East     119787.0
North    160350.0
South    118793.0
West     138415.0
Name: Total Sale Amount, dtype: float64

mean and standard deviation of sales product are:
     Total Sale Amount outliers
0               5180.0   lesser
1               3512.0   lesser
2               4576.0   lesser
3               1250.0   lesser
4               3598.0   lesser
..                 ...      ...
195              937.0   lesser
196             7056.0   lesser
197             1071.0   lesser
198             1086.0   lesser
199             5696.0   lesser

[200 rows x 2 columns]

file saved to C:\Users\hp\Downloads\sales_stored_data.csv
```

## 📊 Visualizations

### Sales by Region
![Sales by Region](Pandas_Matplotlib_projects/Images/DATA_FOR_SALES_AND_SALESPERSON_BAR.png.png)

### Data for sales and salesperson pie
![Data for sales and salesperson pie](Images/DATA_FOR_SALES_AND_SALESPERSON_PIE.png)

### Data for sales and salesperson bar
![Data for sales and salesperson bar](Images/DATA_FOR_SALES_AND_SALESPERSON_BAR.png)

## Sales trend over time
![Sales trend over time](Images/Sale_Trend_Over_Time.png)

## Most sold product
![Most sold product](Images/MOST_SOLD_PRODUCT.png)

---

## 📚 Skills Practiced

- Python Programming
- Data Cleaning & Transformation with Pandas
- Data Aggregation (groupby, sum, mean, etc.)
- Outlier Detection using Mean & Standard Deviation
- Data Visualization with Matplotlib (line plots, bar charts, pie charts)
- Exporting processed data to CSV

---

## 🎯 Future Improvements

- Add interactive visualizations using Plotly / Seaborn
- Automate report generation in PDF/Excel format
- Implement predictive analysis with Machine Learning models
