# task_manager.py

from task import Task

class TaskManager(Task):
    def __init__(self):
        # Initialize TaskManager with an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Method to add a new task to the list
        self.tasks.append(task)

    def edit_task(self, task_name, updates):
        # Method to edit an existing task using a dictionary of updates
        # 'updates' is a dictionary where keys are the attribute names to be updated
        for task in self.tasks:  # Iterate through the list of tasks
            if task.task_name == task_name:  # Find the task by name
                if 'description' in updates:
                    task.set_description(updates['description'])  # Update the description if provided
                if 'priority_level' in updates:
                    task.set_priority(updates['priority_level'])  # Update the priority level if provided
                if 'completion_status' in updates:
                    task.set_completion_status(updates['completion_status'])  # Update the completion status if provided
                return f"Task '{task_name}' updated successfully."  # Return success message
        return f"Task '{task_name}' not found."  # Return error message if task is not found

    def delete_task(self, task_name):
        # Method to delete a task by name
        for task in self.tasks:  # Iterate through the list of tasks
            if task.task_name == task_name:  # Find the task by name
                self.tasks.remove(task)  # Remove the task from the list
                return f"Task '{task_name}' deleted successfully."  # Return success message
        return f"Task '{task_name}' not found."  # Return error message if task is not found

    def view_tasks(self):
        # Method to display all tasks
        if not self.tasks:
            print("No tasks available.")  # Print message if no tasks are in the list
        for task in self.tasks:  # Iterate through the list of tasks
            print(task.display_info())  # Display information for each task

    def sort_tasks_by_priority(self):
        # Method to sort tasks by their priority level
        priority_map = {'low': 1, 'medium': 2, 'high': 3}  # Map priority levels to numbers for sorting
        self.tasks.sort(key=lambda x: priority_map[x.priority_level])  # Sort tasks based on priority
        print("Tasks sorted by priority.")  # Print confirmation message

    def get_overdue_tasks(self):
        # Method to get tasks that are overdue
        from datetime import datetime  # Import datetime module to work with dates
        overdue_tasks = [task for task in self.tasks 
                         if task.completion_status < 100 and datetime.strptime(task.due_date, "%Y-%m-%d") < datetime.now()]
        # Check if task is not completed and due date has passed
        if not overdue_tasks:
            return "No overdue tasks."  # Return message if no tasks are overdue
        return "\n".join(task.display_info() for task in overdue_tasks)  # Return list of overdue tasks
