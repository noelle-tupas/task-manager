# task_manager.py

from task import Task

class TaskManager:
    def __init__ (self):
        '''
            Initializes the TaskManager instance
            
            - The format for due date is MM-DD-YYYYss
            - Priority level can only be high, medium, low
        '''
        self.__tasks = []
        self.__completed_tasks = []
        
    def add_task (self):
        '''
            Allows the user to add a task to the Task Manager
        '''
        task_name = input ('Task name: ')
        description = input ('Description: ')
        due_date = input ('Due date (MM-DD-YYYY): ')
        priority_level = input ('Priority level (low, medium, high): ')
        completion_status = input ('Completion level? (%): ')
        
        new_task = Task (
            task_name,
            description,
            due_date,
            priority_level,
            completion_status
        )
        
        self.__tasks.append(new_task)
        
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
        
        description = input ("New description: ")
        priority_level = input("New priority level (low, medium, high): ")
        completion_status = input("New completion status (%): ")
        
        task.set_description(description)
        task.set_priority(priority_level)
        task.set_completion_status(completion_status)
        
        print ('** Task was edited successfully. **')
        
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
            for task in self.__tasks:
                new_task = task.get_task_details()
                print('>  Task ' + str(self.__tasks.index(task) + 1) + ':')
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
            
        
    # To be implemented
    def get_overdue_tasks (self):
        print ('Get overdue tasks -- not yet implemented')
        
    # Prints the menu
    def print_menu (self):
        print ('---------------------------------------')
        print ('[1] Add Task')
        print ('[2] Edit Task')
        print ('[3] Delete Task')
        print ('[4] View Tasks')
        print ('[5] Sort Tasks by Priority')
        print ('[6] Get Overdue Tasks [Not yet available]')
        print ('---------------------------------------')

tm = TaskManager()

while True:
    tm.print_menu()
    choice = input ("Enter number: ")
    
    if choice == "1":
        print ('[***** ADD TASK ******************]\n')
        tm.add_task()
    elif choice == "2":
        print ('[***** EDIT TASK *****************]\n')
        tm.edit_task()
    elif choice == "3":
        print ('[***** DELETE TASK ***************]\n')
        tm.delete_task()
    elif choice == "4":
        print ('[***** VIEW TASK *****************]\n')
        tm.view_tasks()
    elif choice == "5":
        print ('[***** SORT TASK BY PRIORITY *****]\n')
        tm.sort_tasks_by_priority()
    elif choice == "6":
        print ('[***** GET OVERDUE TASK **********]\n')
        tm.get_overdue_tasks()
    else:
        print ('Invalid input. Please choose [number] from the menu.')
        
