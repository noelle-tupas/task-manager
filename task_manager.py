# task_manager.py

from task import Task

class TaskManager:
    def __init__ (self):
        # Initialize empty list of tasks
        self.__tasks = [] 
        
    # Allows users to add a task to task manager
    def add_task (self):
        # Ask user for task details:
        task_name = input ('Task name: ')
        description = input ('Description: ')
        due_date = input ('Due date (MM-DD-YYYY): ')
        priority_level = input ('Priority level (low, medium, high): ')
        completion_status = input ('Completion level? (%): ')
        
        # Instantiate a new task
        new_task = Task (
            task_name,
            description,
            due_date,
            priority_level,
            completion_status
        )
        
        # Add task to task list
        self.__tasks.append(new_task)
        
    # Allows users to edit a task based on the index of the task
    def edit_task (self):
        task_index = int(input ('Task number: ')) - 1
        if self.__tasks[task_index]:
            # Allow user to change description, priority level and completion status
            description = input ("New description: ")
            priority_level = input("New priority level (low, medium, high): ")
            completion_status = input("New completion status (%): ")
            
            self.__tasks[task_index].set_description(description)
            self.__tasks[task_index].set_priority(priority_level)
            self.__tasks[task_index].set_completion_status(completion_status)
            
            print ('Successfully edited the task\n')
            print (self.__tasks[task_index].get_task_details())
        
    def delete_task (self, task):
        print ('Delete task')
        
    def view_tasks (self):
        for task in self.__tasks:
            new_task = task.get_task_details()
            print('> Task ' + str(self.__tasks.index(task) + 1) + ':')
            print('>  Task name: ' + new_task["Task Name"] + '')
            print('>  Description: ' + new_task["Description"] + '')
            print('>  Due date: ' + new_task["Due Date"] + '')
            print('>  Priority level: ' + new_task["Priority Level"] + '')
            print('>  Completion status: ' + new_task["Completion Status"] + '')
            print ('---------------------------------------')
        
    def sort_tasks_by_priority (self):
        print ('View sorted tasks by priority')
        
    def get_overdue_tasks (self):
        print ('Get overdue tasks')
