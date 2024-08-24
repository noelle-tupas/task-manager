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
        
    # Allows users to delete a task
    def delete_task (self):
        task_index = int(input('Enter the number of the you wish to delete: ')) - 1
        # Checks if chosen task is within the list of tasks
        if 0 <= task_index < len(self.__tasks):
            # Removes the task
            self.__tasks.pop(task_index)
            print('Successfully deleted Task.')
        else:
            print('Invalid task number. Please input a valid task number.')
        
    # Prints all the tasks in the Task Managers
    def view_tasks (self):
        if self.__tasks:
            for task in self.__tasks:
                new_task = task.get_task_details()
                print('> Task ' + str(self.__tasks.index(task) + 1) + ':')
                print('>  Task name: ' + new_task["Task Name"] + '')
                print('>  Description: ' + new_task["Description"] + '')
                print('>  Due date: ' + new_task["Due Date"] + '')
                print('>  Priority level: ' + new_task["Priority Level"] + '')
                print('>  Completion status: ' + new_task["Completion Status"] + '')
                print ('---------------------------------------')
        else:
            print ('No tasks available.')
        
    # To be implemented
    def sort_tasks_by_priority (self):
        if self.__tasks:
            for priority_key in self.__tasks:
                p = priority_key.get_task_details()
                if p["Priority Level"] == 'high':
                    for key, value in p.items():
                        print(f"> {key}: {value}", end='\n')
                    print('---------------------------------------')
            for priority_key in self.__tasks:
                p = priority_key.get_task_details()
                if p["Priority Level"] == 'medium':
                    for key, value in p.items():
                        print(f"> {key}: {value}", end='\n')
                    print('---------------------------------------')

            for priority_key in self.__tasks:
                p = priority_key.get_task_details()
                if p["Priority Level"] == 'low':
                    for key, value in p.items():
                        print(f"> {key}: {value}", end='\n')
                    print('---------------------------------------')
        else:
            print('No tasks available.')
        
    # To be implemented
    def get_overdue_tasks (self):
        print ('Get overdue tasks -- not yet implemented')
        
    # Prints the menu
    def print_menu (self):
        print ('--------- MENU ---------')
        print ('[1] Add Task')
        print ('[2] Edit Task')
        print ('[3] Delete Task')
        print ('[4] View Tasks')
        print ('[5] Sort Tasks by Priority')
        print ('[6] Get Overdue Tasks [Not yet available]')
        print ('-------------------------')

# tm = TaskManager()
# tm.add_task()
# tm.view_tasks()
# tm.edit_task()

tm = TaskManager()

while True:
    tm.print_menu()
    choice = input ("Enter number: ")
    
    if choice == "1":
        print ('[Add Task]')
        tm.add_task()
    elif choice == "2":
        print ('[Edit Task]')
        tm.edit_task()
    elif choice == "3":
        print ('[Delete Task]')
        tm.delete_task()
    elif choice == "4":
        print ('[View Task]')
        tm.view_tasks()
    elif choice == "5":
        print ('[Sort Tasks by Priority]')
        tm.sort_tasks_by_priority()
    elif choice == "6":
        print ('[Get Overdue Tasks]')
        tm.get_overdue_tasks()
    else:
        print ('Invalid input. Please choose [number] from the menu.')
