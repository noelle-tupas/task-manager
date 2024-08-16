# task.py

class Task:
    def __init__ (self, task_name, description, due_date, priority_level, completion_status):
        self.__valid_priority_levels = ['low', 'medium', 'high']
        self.__task_name = task_name
        self.__description = description
        # mm-dd-yyyy
        self.__due_date = due_date
        # low - 0, medium - 1, high - 2
        self.__priority_level = priority_level.lower()
        # Completion status should be in %
        self.__completion_status = completion_status
        
    # Updates the description using user input
    def set_description (self, new_description):
        self.__description = new_description
        
    # Updates the priority level using user input
    def set_priority (self, new_priority_level):
        if self.check_if_valid_priority_level(new_priority_level):
            self.__priority_level = new_priority_level
        else:
            print ('Error: Failed to update priority level. Invalid value provided.')
        
    # Gets the list of valid priority level values
    def get_valid_priority_levels (self):
        return self.__valid_priority_levels
    
    # Checks if the priority level provided by the user is valid
    def check_if_valid_priority_level (self, priority_level):
        valid_priority_levels = self.get_valid_priority_levels()

        if str(priority_level) in valid_priority_levels:
            return True
        
        return False
    
    # Updates the completion status of the task based on user input
    def set_completion_status (self, completion_status):
        self.__completion_status = completion_status
    
    # Gets all of the details of a task
    def get_task_details (self):
        return {
            "Task Name": self.__task_name,
            "Description": self.__description,
            "Due Date": self.__due_date,
            "Priority Level": self.__priority_level,
            "Completion Status": self.__completion_status
        }