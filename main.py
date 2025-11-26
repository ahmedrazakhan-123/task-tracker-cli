import json
import os

def get_tasks():
    # FIXED: 'exists' spelled correctly
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            # FIXED: removed quotes around file
            return json.load(file)
    else:
        return []

# FIXED: Moved to the far Left (un-indented)
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

# FIXED: Moved to the far Left (un-indented)
def main():
    while True:
        print("\nHello, enter your tasks")
        print("1- add task")
        print("2- list tasks")
        print("3- delete tasks")
        print("4- exit")

        choice = input("enter choice (1-4): ")

        if choice == '1':
            description = input("what is the task? ")
            
            # FIXED: Added () to actually run the function
            tasks = get_tasks() 

            new_id = 1
            if len(tasks) > 0:
                new_id = tasks[-1]['id'] + 1

            new_task = {
                'id': new_id,
                'description': description,
                'status': 'todo'
            }
            tasks.append(new_task)
            
            # FIXED: Added (tasks) to pass the data to the function
            save_tasks(tasks)
            print("save tasks")

        elif choice == '2':
            # FIXED: Added ()
            tasks = get_tasks()
            print("\n your tasks")
            for task in tasks:
                # FIXED: formatting of the f-string
                print(f"{task['id']}. [{task['status']}] {task['description']}")

        elif choice == '3':
            # FIXED: Added ()
            tasks = get_tasks()
            id_to_delete = int(input("enter id to delete: "))
            
            # FIXED: Added '=' so the change is actually saved to the variable
            tasks = [t for t in tasks if t['id'] != id_to_delete]
            
            # FIXED: Added (tasks)
            save_tasks(tasks)
            print("task deleted")

        elif choice == '4':
            print('Goodbye')
            break

# FIXED: Moved to the far Left
main()


            



