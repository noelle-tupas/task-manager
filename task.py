# task.py

from datetime import datetime

class Task:
    def __init__ (self, task_name, description, due_date, priority_level, completion_status, type):

        self.__task_name = task_name
        self.__description = description
        self.__due_date = due_date
        self.__priority_level = priority_level
        self.__completion_status = completion_status
        self.__type = type
        
    # Setters
    def set_description (self, new_description):
        '''
            Updates the task's description with the newly provided description
        '''
        self.__description = new_description
        
    def set_priority (self, new_priority_level):
        '''
            Updates the value of the task's priority level
        '''
        self.__priority_level = new_priority_level
    
    def set_completion_status (self, completion_status):
        '''
            Updates the completion status of a task
        '''
        self.__completion_status = completion_status
        
    # Getters
    def get_priority (self):
        '''
            Retrieves the priority level of a task
        '''
        return self.__priority_level
        
    def get_completion_status (self):
        '''
            Retrieves the completion status of a task
        '''
        return self.__completion_status
    
    def get_due_date (self):
        '''
            Retrieves the due date of the task
        '''
        return self.__due_date

    def get_type (self):
        '''
            Returns the task type: Reminder or Task
        '''
        return self.__type
    
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