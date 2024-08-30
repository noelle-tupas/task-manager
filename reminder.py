# reminder.py

from task import Task
from datetime import datetime

class Reminder (Task):
    def __init__ (self, task_name, description, due_date, priority_level, completion_status, type, notification):
        super().__init__ (task_name, description, due_date, priority_level, completion_status, type)
        self.__time_until_deadline = self.compute_time_until_deadline(due_date)
        self.__notification = notification
        
    def compute_time_until_deadline (self, due_date):
        current_date = datetime.now()
        return due_date - current_date
    
    def get_time_until_deadline (self):
        return self.__time_until_deadline
        
    def generate_reminder(self):
        return f'*********\nNotification: {self.__notification}\nTime until deadline: {self.__time_until_deadline}\n*********'
        
    def display_notification(self):
        reminder = self.generate_reminder()
        print (reminder)