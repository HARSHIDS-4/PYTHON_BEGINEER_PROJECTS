#to do list program

import json

items=[]
completed=[]

def load_task():
    file_path="C:\\Users\\hp\\OneDrive\\Desktop\\to_do_list.json"
    with open(file_path,"r") as file:
        content=json.load(file)
        print(content)
    return file_path 


def list():
    while True:
        title=input("enter the to do work list(enter q to quit):").lower()
        if title=="q":
            break
        else:
            status=input("enter the task status (if completed then true else false):").lower()
        items.append({"title":title,"completed":status})
    print()
    print("The Credentials you enterecd are:")
    i=0
    for item in items:
        i=i+1
        print(f"Task[{i}]:{item}")
        
def display_task():
    print("According to them:")
    i=0
    for item in items:
        i=i+1
        if item["completed"]=="true":
            print(f"task{i}:{item['title']}")
            print("     completed✅")    
        elif item["completed"]=="false":
            print(f"task{i}:{item['title']}")
            print("     pending no worries you can still do it😊")
        else:
            print(f"task{i}:{item['title']}")
            print("entered status is incorect❌")


def save_task(file_path):
    write=items
    with open(file_path,"w") as file:
        json.dump(write,file,indent=2)
        print("changes saved in file")


def delete_task():
    for item in items:
        if item["completed"]=="true":
            items.remove(item)
            print(f"title:{item['title']} removed ")
    print()
    print("NEW TO-DO-LIST:")
    for item in items:
        print(f"    title:{item['title']}")


def main():
    print()
    print()
    file_path=load_task()
    print()
    list()
    print()
    display_task()
    print()
    save_task(file_path)
    print()
    delete_task()
if __name__=="__main__":
    main()