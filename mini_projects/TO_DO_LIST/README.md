# ✅ To-Do List Program (Python)

A simple **command-line To-Do List application** built in Python.  
It allows you to **add tasks, mark them as complete/pending, save them to a JSON file, display them, and delete completed tasks**.

---

## 🚀 Features
- Load existing tasks from a JSON file.
- Add new tasks with status (**true/false**).
- Display tasks with:
  - ✅ Completed  
  - 😊 Pending  
  - ❌ Invalid status  
- Save tasks to a JSON file.
- Delete completed tasks from the list.

---

## 💻 How to Run
1. Save the code into a file named `to_do_list.py`.
2. Make sure you have a file `to_do_list.json` in the correct path:
   ```json
   []
- (Start with an empty list.)
3. Run the program:
```bash
python to_do_list.py
```

---

## 📝 Example Run
```
[]   <-- (loaded from JSON)

enter the to do work list(enter q to quit): study python
enter the task status (if completed then true else false): false
enter the to do work list(enter q to quit): gym
enter the task status (if completed then true else false): true
enter the to do work list(enter q to quit): q

The Credentials you entered are:
Task[1]:{'title': 'study python', 'completed': 'false'}
Task[2]:{'title': 'gym', 'completed': 'true'}

According to them:
task1:study python
     pending no worries you can still do it😊
task2:gym
     completed✅

changes saved in file

title:gym removed 

NEW TO-DO-LIST:
    title:study python
```

**Happy coding!**
**— Harshi Gupta ✨**
