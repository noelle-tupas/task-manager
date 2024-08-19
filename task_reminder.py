from datetime import datetime

class TaskReminder:
    def __init__(self, due_date):
        # mm-dd-yyyy HH:MM (24-hour format)
        self.__due_date = datetime.strptime(due_date, "%m-%d-%Y %H:%M")
        self.__reminder_sent = False
        self.__overdue_reminder = False

    def check_due_date(self):
        #Check due date#
        current_time = datetime.now()
        #Sends reminder if not yet sent#
        if current_time >= self.__due_date and not self.__reminder_sent:
            self.send_reminder()
            self.__reminder_sent = True
        
    def prompt_overdue_date(self):
        #When the task is overdue
        now = current_time.strftime("%d")
        due = self.__due_date.strftime("%d")
        overdue = due - now
        if overdue == 1:
            self.send_overdue_reminder()
            self.__overdue_reminder = True
    
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
        
        
