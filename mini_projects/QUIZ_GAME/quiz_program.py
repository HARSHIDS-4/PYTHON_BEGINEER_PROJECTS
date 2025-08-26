#quiz program

questions=(("QUESTION.1 Which symbol is used in python to add comments?"),("QUESTION.2 Which type of brackets are used to create list?"),("QUESTION2.3 Which of the following is the extension for creating python file?"),("QUESTION.4 Which of the following is correct for sets?"))

options=(("a.#","b.//","c.\\","d./*") , ("a.[]", "b.{}", "c.()" , "d.none of these") , ("a.py" , "b.c" , "c.cpp" , "d.pt") , ("a.[]", "b.{}", "c.()" , "d.none of these"))

index=0
answers=("a", "a" , "a" , "b")
guess=[]
for question in questions:
    print("--------------------------------------------------------------------------------")
    print(question)

    
    for option in options[index]:
        print(option)
    print()

    choice=str(input("enter your choice:"))

    if choice not in ("a","b","c","d"):
        print("enter a valid choice")
        break
    
    elif choice==answers[index]:
        print("CORRECT!")
    else:
        print(f"INCORRECT: correct answer is {answers[index]}")

    print()
    index=index+1
    
    guess.append(choice)
for choosen in guess:
    print(choosen,end=" ")
print()


for answer in answers:
    print(answer,end=" ")