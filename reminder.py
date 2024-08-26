# reminder.py

from datetime import datetime, timedelta

class Reminder:
    def __init__(self, task):
        # Extract due date and other task details
        self.task = task
        self.__due_date = datetime.strptime(task.get_task_details()['Due Date'], "%m-%d-%Y")
        self.__reminder_sent = False
        self.__overdue_reminder = False
        self.__upcoming_task_reminder = False
        self.time_until_deadline = None
        self.notifications = None

    def generateReminder(self):
        self.check_due_date()
        self.prompt_overdue_date()
        self.prompt_upcoming_tasks()

    def displayNotification(self):
        if self.notifications:
            print(self.notifications)
        else:
            print("No notifications at the moment.")

    def check_due_date(self):
        current_time = datetime.now()
        self.time_until_deadline = self.__due_date - current_time
        if current_time >= self.__due_date and not self.__reminder_sent:
            self.send_reminder()
            self.__reminder_sent = True

    def prompt_overdue_date(self):
        now = datetime.now()
        if now > self.__due_date and not self.__overdue_reminder:
            self.send_overdue_reminder()
            self.__overdue_reminder = True

    def prompt_upcoming_tasks(self):
        now = datetime.now()
        upcoming = self.__due_date - now
        if 0 < upcoming <= timedelta(days=1) and not self.__upcoming_task_reminder:
            self.send_upcoming_tasks()
            self.__upcoming_task_reminder = True

    def send_reminder(self):
        # Reminder message
        self.notifications = f"Reminder: The task '{self.task.get_task_details()['Task Name']}' is due on {self.__due_date.strftime('%m-%d-%Y')}!"
        print("-------------------------")
        print(self.notifications)
        print("-------------------------")

    def send_overdue_reminder(self):
        # Sends reminder when task is overdue
        self.notifications = f"Reminder: The task '{self.task.get_task_details()['Task Name']}' is overdue! Please check your task manager."
        print("-------------------------")
        print(self.notifications)
        print("-------------------------")

    def send_upcoming_tasks(self):
        # Sends upcoming task reminder
        self.notifications = f"Reminder: The task '{self.task.get_task_details()['Task Name']}' is due soon! Please check your task manager."
        print("-------------------------")
        print(self.notifications)
        print("-------------------------")
        
    def get_task_details(self):
        '''
            Returns the original task object
        '''
        return self.task
