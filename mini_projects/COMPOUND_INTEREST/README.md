# 💰 Compound Interest Calculator

A simple Python program to calculate the **final amount** using the **Compound Interest formula** with user input validation.  

---

## 📌 Formula Used

\[
A = P \times \left(1 + \frac{R}{100}\right)^T
\]

Where:  
- **P** = Principal Amount  
- **R** = Rate of Interest (in %)  
- **T** = Time Period (in days)  
- **A** = Final Amount  

---

## 📌 Features

- Validates user input (no zero or negative values).  
- Calculates compound interest based on the given values.  
- Shows step-by-step entered values before final calculation.  

---

## 📦 Requirements

- Python 3.x  

---

## 🚀 How to Run

1. Clone this repository (or copy the file to your system).  

2. Open terminal and run:  
   ```bash
   python compound_interest.py

3. Enter values for:
    - Principal
    - Interest Rate (%)
    - Time Period (in days)

---

## 🎯 Example Run
```
enter the principal value: 1000
principle value is: 1000.0

enter the interest rate(in percentage): 5
the interest rate is: 5.0

enter the time period(in days): 2
the value of time period entered is: 2.0

the final amount is: 1102.5
```

---

## 📚 Skills Practiced
- Loops (while)
- Input validation
- Mathematical calculations with pow()
- Printing formatted results

---

## 📝 Notes

- This version assumes daily compounding based on the given time in days.
- You can enhance it by:
    - Allowing different compounding periods (yearly, monthly, quarterly).
    - Showing compound interest separately (CI = A - P).
    - Exporting results to a file or database.