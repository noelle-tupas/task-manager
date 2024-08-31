from task import Task
from reminder import Reminder
from datetime import datetime

class TaskManager:
    def __init__ (self):
        self.__tasks = []
        self.__completed_tasks = []
        
    def print_menu (self):
        '''
            Prints the menu of the Task Manager app
        '''
        print ('---------------------------------------')
        print ('[1] Add Task')
        print ('[2] Edit Task')
        print ('[3] Delete Task')
        print ('[4] View Tasks')
        print ('[5] Sort Tasks by Priority')
        print ('[6] Get Overdue Tasks')
        print ('[7] Get Reminders')
        print ('---------------------------------------')
        
    def add_task (self):
        '''
            Allows the user to add a task to the Task Manager
        '''
        
        '''
            This code block validates all the user input relevant
            to the creation of a Task, it will keep on looping until
            the user provides a valid value.
        '''
        while True: 
            task_name = input ('Enter task name: ').strip()
            
            if task_name:
                break
            else:
                print ('Invalid input, task name cannot be empty.')
                
        while True: 
            description = input ('Enter task description: ').strip()
            
            if description:
                break
            else:
                print ('Invalid input, task name cannot be empty.')
                
        while True: 
            due_date = input ('Enter task deadline (mm-dd-yyyy): ').strip()
            
            if due_date:
                if datetime.strptime (due_date, '%m-%d-%Y'):
                    if datetime.strptime (due_date, '%m-%d-%Y') > datetime.now():
                        due_date = datetime.strptime(due_date, '%m-%d-%Y')
                        break
                    else:
                        print ('Invalid input, deadline cannot precede current date.')
                else:
                    print ('Invalid input, please follow the format mm-dd-yyyy')
            else:
                print ('Invalid input, task name cannot be empty.')
                
        while True:
            priority_level = input ('Enter priority level (low, medium, high): ').strip().lower()
            
            if priority_level:
                if priority_level in ['low', 'medium', 'high']:
                    break
                else:
                    print ('Invalid input, priority level can only be low, medium, or high.')
            else:
                print ('Invalid input, priority level cannot be empty.')
        
        while True:        
            completion_status = input ('Enter completion status (%): ')
            if completion_status:
                if '%' in completion_status:
                    completion_status_for_validation = int(completion_status.replace('%', ''))
                    if completion_status_for_validation >= 0 and completion_status_for_validation <= 100:
                        break
                    else:
                        print ('Invalid input, completion status must be only be 0-100%')
                else:
                    print ('Invalid input. Completion status must be suffixed by % (ex. 90%, 30%)')
            else:
                print ('Invalid input. Completion status cannot be empty.')
        
        '''
            Verify if the user wants to create a task or a task with reminder
        '''
        while True:
            reminder_choice = input('Would you like a reminder? (yes/no): ').strip().lower()

            if reminder_choice == 'yes' or reminder_choice == 'no':
                break
            else:
                print ('Invalid input, accepted values can only be yes or no')


        '''
            If the user enters yes, then the program will prompt the user for a notification message,
            if not, then the program proceeds to creating a new Task
        '''
        if reminder_choice == 'yes':
            while True:
                notification_message = input ("Enter your desired notification message for the reminder.").strip()
                
                if notification_message:
                    break
                else:
                    print ('Invalid input, notification message cannot be empty.')
            
            new_task = Reminder(task_name, description, due_date, priority_level, completion_status, "Reminder", notification_message)
        else:
            new_task = Task(task_name, description, due_date, priority_level, "Task", completion_status)
        
        self.__tasks.append(new_task)
        
        print("Task added successfully!")

    def edit_task (self):
        '''
            Allows the user to edit an existing task
        '''
        index = int(input ('Enter the number of the task you wish to edit: ')) - 1
        
        if not index >= 0 and index < len(self.__tasks):
            '''
                Checks if the index is valid. If not, it will
                end the execution of the method, else it will
                continue with the rest of the method
            '''
            print ('Task does not exist. Try again.')
            return
        
        task = self.__tasks[index]
        
        while True: 
            description = input ('Enter new task description: ').strip()
            
            if description:
                break
            else:
                print ('Invalid input, task name cannot be empty.')
                
        while True:
            priority_level = input ('Enter new priority level (low, medium, high): ').strip().lower()
            
            if priority_level:
                if priority_level in ['low', 'medium', 'high']:
                    break
                else:
                    print ('Invalid input, priority level can only be low, medium, or high.')
            else:
                print ('Invalid input, priority level cannot be empty.')
        
        while True:        
            completion_status = input ('Enter new completion status (%): ')
            if completion_status:
                if '%' in completion_status:
                    completion_status_for_validation = int(completion_status.replace('%', ''))
                    if completion_status_for_validation >= 0 and completion_status_for_validation <= 100:
                        break
                    else:
                        print ('Invalid input, completion status must be only be 0-100%')
                else:
                    print ('Invalid input. Completion status must be suffixed by % (ex. 90%, 30%)')
            else:
                print ('Invalid input. Completion status cannot be empty.')
        
        '''
            Utilize the task setters to update
            the values of these task attributes
        '''
        task.set_description(description)
        task.set_priority(priority_level)
        task.set_completion_status(completion_status)
        
        print ('*** Task was edited successfully! ***')
        
        '''
            Check if the task is already completed (100%). If yes, move it to
            the completed tasks list
        '''
        if task.get_completion_status() == '100%':
            self.__tasks.remove(task)
            self.__completed_tasks.append(task)
            
    def delete_task (self):
        '''
            Allows the user to delete a task given a valid index
        '''
        index = int(input('Enter the number of the task you wish to delete: ')) - 1
        
        if not index >= 0 and index < len(self.__tasks):
            '''
                Checks if the index is valid. If not, it will
                end the execution of the method, else it will
                continue with the rest of the method
            '''
            print ('Task does not exist. Try again.')
            return
            
        task = self.__tasks[index]
        
        choice = input ('Are you sure you want to delete this task? Y/n:')
        
        if choice.lower() == 'y':
            self.__tasks.remove(task)
            print ('Task successfully deleted')
        else:
            print ('Operation aborted.')
            return
        
    def view_tasks (self):
        '''
            Allows the user to view all tasks
        '''
        if self.__tasks or self.__completed_tasks:
            print ('\n[***** ONGOING TASKS *****]')
            for task in self.__tasks:
                new_task = task.get_task_details()
                print('>  Task ' + str(self.__tasks.index(task) + 1) + ':')
                for key, value in new_task.items():
                    print(f">  {key}: {value}", end='\n')
                print('---------------------------------------')

            print ('\n[***** COMPLETED TASKS *****]')
            for task in self.__completed_tasks:
                new_task = task.get_task_details()
                print('>  Task ' + str(self.__completed_tasks.index(task) + 1) + ':')
                for key, value in new_task.items():
                    print(f">  {key}: {value}", end='\n')
                print ('---------------------------------------')
        
        else:
            print ('No available tasks.')
        
    def get_priority_mapping (self, task):
        '''
            Maps a priority level to a specific value to be used for sorting
            Low is 0, Medium is 1, High is 2
        '''
        task_priority_level = task.get_priority().lower()
        
        if task_priority_level == 'low':
            return 0
        elif task_priority_level == 'medium':
            return 1
        else:
            return 2
        
    def sort_tasks_by_priority (self):
        '''
            Allows the user to sort the task list by priority and prints the sorted
            list. This does not override the original task list
        '''
        to_be_sorted = self.__tasks
        
        '''
            Used lambda to use extract an element of to_be_sorted and use it for get_priority_mapping
            to be used a sort key since get_priority_mapping requires access to attributes of task
        '''
        to_be_sorted.sort(key=lambda task: self.get_priority_mapping(task))
        
        print ('\n[***** SORTED TASKS *****]')
        for task in to_be_sorted:
            new_task = task.get_task_details()
            print('>  Task ' + str(self.__tasks.index(task) + 1) + ':')
            for key, value in new_task.items():
                print(f">  {key}: {value}", end='\n')
            print('---------------------------------------')
            
    def get_overdue_tasks (self):
        current_date = datetime.now()
        
        for task in self.__tasks:
            deadline = task.get_due_date()
            print (deadline)
            print (current_date)
            print (deadline - current_date)
            if (deadline < current_date):
                
                task_number = self.__tasks.index(task)
                '''
                    Print task details
                '''
                task_details = task.get_task_details()
                print (f'> Task No: {task_number}')
                for key, value in task_details.items():
                    print (f'> {key}: {value}', end='\n')
                print('---------------------------------------')
                
    def get_reminders (self): 
        ''' 
            View all tasks with notification/reminders
        '''
        task_list = self.__tasks
        for task in task_list:
            if task.get_type() == 'Reminder':
                task_number = task_list.index(task)
                '''
                    Print reminder details
                '''
                task.display_notification()
                task_details = task.get_task_details()
                print (f'> Task No: {task_number}')
                for key, value in task_details.items():
                    print (f'> {key}: {value}', end='\n')
                print('---------------------------------------')
        
tm = TaskManager()

while True:
    tm.print_menu()
    choice = input ("Enter number: ")
    
    if choice == "1":
        print ('[***** Add Task ******************]\n')
        tm.add_task()
    elif choice == "2":
        print ('[***** Edit Task *****************]\n')
        tm.edit_task()
    elif choice == "3":
        print ('[***** Delete Task ***************]\n')
        tm.delete_task()
    elif choice == "4":
        print ('[***** View Task *****************]\n')
        tm.view_tasks()
    elif choice == "5":
        print ('[***** Sort Task By Priority *****]\n')
        tm.sort_tasks_by_priority()
    elif choice == "6":
        print ('[***** Get Overdue Task **********]\n')
        tm.get_overdue_tasks()
    elif choice == "7":
        print ('[***** Get Reminders *************]\n')
        tm.get_reminders()
    else:
        print ('Invalid input. Please choose [number] from the menu.')
