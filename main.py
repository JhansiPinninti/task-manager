from task_manager import TaskManager

def main():
    manager = TaskManager("tasks.json")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. View Upcoming Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Export Tasks to CSV")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            #Add Task
            title = input("Task title: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority= input("Priority (High/Medium/Low): ")
            manager.add_task(title, due_date,priority)

        elif choice == '2':
            #View Taks
            manager.view_tasks()

        elif choice == '3':
            #View Upcoming Tasks
            manager.view_upcoming_tasks()

        elif choice == '4':
            #Complete Task
            index = int(input("Enter task number to complete: ")) - 1
            manager.complete_task(index)

        elif choice == '5':
            #Delete Task
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)

        elif choice == '6':
            #Export to CSV
            manager.export_to_csv()

        elif choice == '7':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
