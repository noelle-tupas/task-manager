# task.py

class Task:
    def __init__ (self, task_name, description, due_date, priority_level, completion_status=False):
        '''
            Initializes the Task instance
            
            - The format for due date is MM-DD-YYYYss
            - Priority level can only be high, medium, low
            - Completion status is False by default
        '''
        self.__valid_priority_levels = ['low', 'medium', 'high']
        self.__task_name = task_name
        self.__description = description
        self.__due_date = due_date
        self.__priority_level = priority_level.lower()
        self.__completion_status = completion_status
        self.__archieve = []
        
    def set_description (self, new_description):
        '''
            Updates the task's description with the newly provided description
        '''
        self.__description = new_description
        
    def set_priority (self, new_priority_level):
        '''
            Updates the priority of a task with the newly provided priority.
            It also calls check_if_valid_priority_level to verify if the priority
            level is either low, medium, or high. Else, it will print an error
        '''
        if self.check_if_valid_priority_level(new_priority_level):
            self.__priority_level = new_priority_level
        else:
            print ('Error: Failed to update priority level. Invalid value provided.')
            
    def get_priority (self):
        '''
            Retrieves the priority level of a task
        '''
        return self.__priority_level
        
    def get_valid_priority_levels (self):
        '''
            Retrieves all valid priority levels defined
        '''
        return self.__valid_priority_levels
    
    def check_if_valid_priority_level (self, priority_level):
        '''
            Validates the new priority entered by the user and returns
            either True or False
        '''
        valid_priority_levels = self.get_valid_priority_levels()

        if str(priority_level) in valid_priority_levels:
            return True
        
        return False
    
    def set_completion_status (self, completion_status):
        '''
            Updates the completion status of a task
        '''
        self.__completion_status = completion_status
        
    def get_completion_status (self):
        '''
            Retrieves the completion status of a task
        '''
        return self.__completion_status
    
    def get_task_details (self):
        '''
            Returns an object containing all relevant information
            about a task
        '''
        return {
            "Task Name": self.__task_name,
            "Description": self.__description,
            "Due Date": self.__due_date,
            "Priority Level": self.__priority_level,
            "Completion Status": self.__completion_status
        }
    
    def mark_as_completed(self):
        '''
            Marks the task as completed and stores it in the archieve
        '''
        if not self.__completion_status:
            self.__completion_status = True
            self.archieve_task()
            print(f'Task "{self.__task_name}" has been marked as completed.')
        else:
            print(f'Task "{self.__task_name}" is already completed.')

    def archive_task(self):
        '''
            Archives the completed task for reference
        '''
        if self.__completion_status:
            task_details = self.get_task_details()
            self.__archieve.append(task_details)
            print(f'Task "{self.__task_name}" has been archived.')

    def view_archieve(self):
        '''
            View all archived tasks
        '''
        if self.__archieve:
            print("Archived Tasks:")
            for idx, task in enumerate(self.__archieve, start=1):
                print(f"\nTask {idx}:")
                for key, value in task.items():
                    print(f"{key}: {value}")

        else:
            print("No tasks have been archived yet")