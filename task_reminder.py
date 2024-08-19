from datetime import datetime, timedelta

class TaskReminder:
    def __init__(self, due_date):
        # mm-dd-yyyy HH:MM (24-hour format)
        self.__due_date = datetime.strptime(due_date, "%m-%d-%Y %H:%M")
        self.__reminder_sent = False
        self.__overdue_reminder = False
        self.__upcoming_task_reminder = False

    def check_due_date(self):
        #Check due date#
        current_time = datetime.now()
        #Sends reminder if not yet sent#
        if current_time >= self.__due_date and not self.__reminder_sent:
            self.send_reminder()
            self.__reminder_sent = True
        
    def prompt_overdue_date(self):
        #When the task is overdue
        now = datetime.now()
        overdue = now - self.__due_date
        int_overdue = overdue.days
        if int_overdue == 1:
            self.send_overdue_reminder()
            self.__overdue_reminder = True

    def prompt_upcoming_tasks(self):
        now = datetime.now()
        upcoming = self.__due_date - now
        int_upcoming = upcoming.days
        if int_upcoming == 1:
            self.send_upcoming_tasks()
            self.__upcoming_task_reminder = True
    
    def send_reminder(self):
        #Reminder message#
        print("-------------------------")
        print(" ")
        print(f"Reminder: The task is due on {self.__due_date.strftime('%m-%d-%Y %H:%M')}!")
        print(" ")
        print("-------------------------")
    
    def send_overdue_reminder(self):
        #Sends reminder when task is overdue
        print("-------------------------")
        print(" ")
        print("Reminder: You have an overdue task! Please check your task manager.")
        print(" ")
        print("-------------------------")

    def send_upcoming_tasks(self):
        #Sends upcoming tasks
        print("-------------------------")
        print(" ")
        print("Reminder: Upcoming Task(s)")
        print("")
        print("Wala pa :P")
        print(" ")
        print("-------------------------")
        
        
