#to do list

class TodoList:
    def __init__(self):
        self.task=[]

    def addT(self,task_input):
        self.task.append({"Task":task_input,"Complete":False})
        for e,t in enumerate(self.task,start=1):
            if t["Complete"]:
                status = "Complete ✅"
            else:
                status = "Pending... ❌"
            print(f"{e}) {t['Task']} - {status}")

    def showT(self):
        if len(self.task)==0:
            print("No Tasks Yet!")
            return
        for index,all_task in enumerate(self.task,start=1):
            if all_task["Complete"]:
                status = "Complete ✅"
            else:
                status = "Pending... ❌"
            print(f"{index}) {all_task['Task']} - {status}")
            

    def removeT(self,index):
        if len(self.task)==0:
            print("No Tasks Yet!")
            return
        if index<=len(self.task):
            rem=self.task.pop(index-1)
            print(f"Removed task: {rem['Task']}")
            print("Updated List:")
            for e,t in enumerate(self.task,start=1):
                if t["Complete"]:
                    status="Complete ✅"
                else:
                    status= "Pending... ❌"
                print(f"{e}) {t['Task']} - {status}")
        else:
            print("Invalid Task Number")
                

    def totalT(self):
        print("Total Tasks:", len(self.task))

    def completedT(self):
        c=0
        for e,t in enumerate(self.task,start=1):
            if t["Complete"]:
                print(f"{e}) {t['Task']}")
                c+=1
        print("Completed Tasks:",c)

    def incompleteT(self):
        c=0
        for e,t in enumerate(self.task,start=1):
            if t["Complete"]==False:
                print(f"{e}) {t['Task']}")
                c+=1
        print("Incomplete Tasks:",c)

    def markComplete(self,index):
        if 0<index<=len(self.task):
            self.task[index-1]["Complete"] = True
            print(f"Task '{self.task[index-1]['Task']}' marked as Complete ✅")
        else:
            print("Invalid Task Number")

    def clearT(self):
        self.task.clear()
        print("All Tasks Cleared!")

    def saveToFile(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.task:
                file.write(f"{task['Task']}|{task['Complete']}\n")
            print("Tasks saved successfully!")

todo = TodoList()

while True:
    print("\n==== TODO LIST MENU ====")
    print("1) Add Task")
    print("2) Show All Tasks")
    print("3) Remove Task")
    print("4) Mark Task Complete")
    print("5) Show Completed Tasks")
    print("6) Show Incomplete Tasks")
    print("7) Total Tasks")
    print("8) Clear All Tasks")
    print("9) Save to a Text File")
    print("0) Exit")

    choice =int(input("Enter your choice: "))

    if choice==1:
        task_name=input("Enter you task:")
        todo.addT(task_name)
        
    elif choice==2:
        todo.showT()

    elif choice==3:
        idx=int(input("Enter the task number to be removed:"))
        todo.removeT(idx)

    elif choice==4:
        idx = int(input("Enter task number to mark complete: "))
        todo.markComplete(idx)

    elif choice==5:
        todo.completedT()

    elif choice==6:
        todo.incompleteT()

    elif choice==7:
        todo.totalT()

    elif choice==8:
        todo.clearT()

    elif choice==9:
        todo.saveToFile()

    elif choice==0:
        print("Exiting...")
        print("==========================================")
        break
    
    else:
        print("Invalid choice! Please try again.")
        
        
                
        


        
        
        
