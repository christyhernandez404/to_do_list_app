import os
import time

task_app = {
    1: {'Notes': "buy bread, ham, cheese", 'Status': 'To Do'},
    2: {'Notes': "go to doctor's appointment", 'Status': 'Done'}
}

#1, 2 are the keys of the outer dictionary
def add_task():
    while True:
        Notes = input("Type in your note: ")
        Status = 'To Do'
        print(f"Notes: {Notes}, Status: {Status}")
        correct = input("Is this information accurate? y/n ")
        if correct.lower() == 'y':
            new_id = max(task_app.keys()) + 1
            task_app[new_id] = {'Notes': Notes, 'Status': Status}  
            break
        else:
            continue


def view_tasks():
    print("Here are your tasks:")
    for task_id, task_info in task_app.items():
        print(f"ID: {task_id}, Notes: {
              task_info['Notes']}, Status: {task_info['Status']}")


def mark_complete():
    print("\nPlease view tickets first to see which ticket number you'd like to update")
    instead_quit = input(
        "\nIf instead you'd like to go back to the main menu,  type main menu and press Enter. \nIf you know the task number you'd like to mark complete press Enter to go to the next prompt.")
    if instead_quit == 'main menu':
        return 
    try:
        task_id = int(input("Type in the task number you'd like to mark complete"))
        if task_id in task_app:
            task_app[task_id]['Status'] = 'Done'
            print(f"The task has been updated: ID: {task_id}, Notes: {task_app[task_id]['Notes']}, Status: {
                  task_app[task_id]['Status']}")
        else:
            if task_id not in task_app:
                print("Invalid task number")
    except ValueError:
        print("Invalid input. Please enter a valid task number")
    except Exception as e:
        print(f"An error occured:{e}")


def delete_task():
    task_id = int(input("Type in the task number you'd like to delete: "))
    if task_id in task_app:
        confirm = input("Please confirm you'd like to delete this task: y/n ")
        if confirm.lower() == 'y':
            del task_app[task_id] 
            print(f"Task {task_id} has been deleted")
        else:
            print("Deletion cancelled")
    else:
        print("Invalid task number. No task ID found.")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    while True:  
        ans = input('''
Welcome to the To-Do List App!
                    
1. Add a task
2. View tasks
3. Mark a task complete
4. Delete a task
5. Quit

Enter the corresponding number for the action you'd like to take here: ''')
        if ans == '1':
            add_task()
            clear()
        elif ans == '2':
            view_tasks()
            time.sleep(6)
            clear()
        elif ans == '3':
            mark_complete()
            time.sleep(6)
            clear()
        elif ans == '4':
            delete_task()
            time.sleep(6)
            clear()
        elif ans == '5':
            print("Thanks for using the To-Do List app!")
            break
        else:
            print("Invalid data entry. Try again")


main()


