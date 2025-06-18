import json
import os

def list_view():
    print("\nTASKS")
    if len(Tasks) > 0:
        for index, task in enumerate(Tasks, start=1):
            title = task["title"]
            due = task["due"]
            print(f"{index}. {title}: {due}")
        print(f"Tasks: {len(Tasks):>2}".rjust(50))
    else:
        print("\nAll caught up!")
        
def add_task():
    print("\nNew Task:")
    title = input("Task: ")
    due = input("Due: ")
    task = {"title": title, "due": due}
    Tasks.append(task)
    print(f"{title} has been successfully added.")
    
def remove_task():
    if not Tasks:
        print("There are no tasks at this time.")
        return
    else:
        list_view()
        print("\nPlease select task number to remove:")
        try:
            task_index = int(input("> ")) - 1
            task = Tasks.pop(task_index)
            title = task["title"]
            print(f"{title} has been removed")    
        except ValueError:
            print("Please enter the task's index number.")
        except IndexError:
            print("That task is not on the list.")

def save_file():
    print("Saving...")
    with open("Tasks.json", 'w') as f:
        json.dump(Tasks, f)
        
def clear_term(): #Clears the terminal for commandline stuff
    os.system("cls" if os.name == "nt" else "clear") # type: ignore
        
def main():
    while True:
        clear_term()
        menu = [
            "List Tasks",
            "Add Task",
            "Remove Task",
            "Quit",
        ]
        print("\nMENU:")
        for index, option in enumerate(menu, start=1):
            print(f"{index}. {option}")
        try:
            selection = int(input("Please select a number: > "))
            clear_term()
            if selection == 1:
                list_view()
            elif selection == 2:
                add_task()
                save_file()
            elif selection == 3:
                remove_task()
                save_file()
            else:
                confirm = input("Exit? (y/n): > ").lower()
                if confirm == "y":
                    save_file()
                    print("Exiting...")
                    break
            input("\nPress Enter to continue...")
        except ValueError:
            print("Please select a number.")
            input("\nPress Enter to continue...")
        except IndexError:
            print("Please choose a valid option.")
            input("\nPress Enter to continue...")
try:
    with open("Tasks.json", "r") as f:
        Tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    Tasks = []
main()    