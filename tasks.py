import json

def list_view():
    print("\nTASKS")
    if len(Tasks) > 0:
        for index, task in enumerate(Tasks, start=1):
            title = task["title"]
            due = task["due"]
            print(f"{index}. {title}: {due}")
        print(f"Tasks: {len(Tasks):>2}".rjust(50))
        input("\nPress Enter to continue...")
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
        
def main():
    while True:
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
            if selection == 1:
                list_view()
                input("\nPress Enter to continue...")
            elif selection == 2:
                add_task()
            elif selection == 3:
                remove_task()
            else:
                save_file()
                print("Exiting...")
                break
        except ValueError:
            print("Please select a number.")
        except IndexError:
            print("Please choose a valid option.")
try:
    with open("Tasks.json", "r") as f:
        Tasks = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    Tasks = []
main()    