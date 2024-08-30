# reminder.py

from task import Task
from datetime import datetime

class Reminder (Task):
    def __init__ (self, task_name, description, due_date, priority_level, completion_status, type, notification):
        super().__init__ (task_name, description, due_date, priority_level, completion_status, type)
        self.__time_until_deadline = self.compute_time_until_deadline(due_date)
        self.__notification = notification
        
    def compute_time_until_deadline (self, due_date):
        '''
            Computes the difference between the due date provided
            and the current time output via datetime.now()
        '''
        current_date = datetime.now()
        return due_date - current_date
        
    def generate_reminder(self):
        '''
            Returns the reminder message which is just
            the notification message the user has set and
            the time until the deadline specified
        '''
        return f'*********\nNotification: {self.__notification}\nTime until deadline: {self.__time_until_deadline}\n*********'
        
    def display_notification(self):
        '''
            Displays the reminder message that we have generated
            via generate_reminder()
        '''
        reminder = self.generate_reminder()
        print (reminder)
        
    # Getters
    def get_time_until_deadline (self):
        '''
            Returns the time remaining until deadline
        '''
        return self.__time_until_deadline