import csv
import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self,title, due_date, priority):
        self.tasks.append({
            "title": title,
            "due_date": due_date,
            "priority": priority,
            "completed": False
        })
        self.save_tasks()
        print(f"Task '{title}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            due = task.get("due_date","N/A")
            priority = task.get("priority", "N/A")
            print(f"{i}. [{status}] {task['title']} (Due: {task['due_date']}, Priority: {task['priority']})")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")

    def view_upcoming_tasks(self):
        today = datetime.today().date()
        upcoming = [t for t in self.tasks if not t["completed"] and datetime.strptime(t["due_date"], "%Y-%m-%d").date() >= today]
        if not upcoming:
            print("No upcoming tasks.")
            return
        for i, task in enumerate(upcoming, start=1):
            print(f"{i}. {task['title']} (Due: {task['due_date']})")

    def export_to_csv(self, filename="tasks.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "due_date", "priority", "completed"])
            writer.writeheader()
            writer.writerows(self.tasks)
        print(f"✅ Tasks exported to {filename}")


