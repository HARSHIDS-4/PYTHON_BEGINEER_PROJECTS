# 🎟️ Concession Stand Program

Hi there!   
This is a simple Python project I built to practice basic programming concepts like functions, dictionaries, user input,file handling and formatting output in a fun way.

The idea is to simulate a digital **concession stand** — like the kind you’d see at a movie theater or a school event. It shows a menu, lets you choose items and quantities, calculates your total bill, and prints a neat receipt with the current date and time.it can even store your previous receipt.

---

## 🧾 What It Does

- Displays your previous receipt
- Shows a menu of snacks and drinks with prices
- Lets users choose items and enter how many they want
- Asks for coupon
- Calculates the total cost
- Prints a formatted receipt 
- Displays the date and time of purchase

--- 

## 💻 Technologies Used

- Python 3
- Standard libraries (`datetime`,`json`)

---

## Note
`concession_stand_receipt.json` is excluded from this repo as it is user-specific and changes every run.

---

## 🧾 Sample Output
```
{'items': ['Pizza', 'Popcorn'], 'quantity': [2, 1], 'unit price': [500, 300], 'price': [1000, 300], 'coupon': False, 'date': '2025-08-01', 'time': '02:51:31', 'total': 1300}
WELCOME TO THE CONCESSION STAND!!

-----------MENU📜-------------   
Popcorn               300        
Pizza                 500        
Sandwich              150
Nachos And Cheese     350
Hot Dog               150
Candy                 60
Mineral Water         50
Coffee                100
Hot Chocolate         110
Soda                  70
Smoothie              170
----------------------------
select an item(q to quit)🍽: popcorn
enter the quantity of Popcorn you want:2
select an item(q to quit)🍽: candy
enter the quantity of Candy you want:3
select an item(q to quit)🍽: soda
enter the quantity of Soda you want:4
select an item(q to quit)🍽: sandwich
enter the quantity of Sandwich you want:1
select an item(q to quit)🍽: q
Do you have coupon?(yes or no)no

------------------------------YOUR RECEIPT---------------------------------------
item                 quantity             unit price                price        
---------------------------------------------------------------------------      
Popcorn              2                    300                         600        
Candy                3                    60                          180        
Soda                 4                    70                          280        
Sandwich             1                    150                         150        
---------------------------------------------------------------------------      
TOTAL                                                              1210
---------------------------------------------------------------------------------
2025-08-07
21:32:58.971752
✅ Receipt saved successfully.
```

## ▶️ How to Run It

1. Make sure you have Python installed on your system.
2. Clone this repo:
   git clone https://github.com/HARSHIDS-4/concession-stand.git
   
3.Navigate into the folder:
  cd folder_name.
  
4.Run the program:
  python: concession_stand_program.py.
  
You’ll be greeted with a welcome message and the menu. From there, just type in your order and let the program do the rest!

---

🙋‍♀️ Why I Made This
I built this as one of my first Python mini-projects to get more confident with core concepts. If you're just starting out, feel free to fork this repo, play around with it, and make it your own!

Happy coding!
— Harshi Gupta ✨
