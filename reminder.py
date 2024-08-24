from datetime import datetime, timedelta

class Reminder:
    def __init__(self, due_date):
        # mm-dd-yyyy HH:MM (24-hour format)
        self.__due_date = datetime.strptime(due_date, "%m-%d-%Y %H:%M")
        self.__reminder_sent = False
        self.__overdue_reminder = False
        self.__upcoming_task_reminder = False

    def check_due_date(self):
        current_time = datetime.now()
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
        #Reminder message#
        print("-------------------------")
        print(f"Reminder: The task is due on {self.__due_date.strftime('%m-%d-%Y %H:%M')}!")
        print("-------------------------")

    def send_overdue_reminder(self):
        #Sends reminder when task is overdue#
        print("-------------------------")
        print("Reminder: You have an overdue task! Please check your task manager.")
        print("-------------------------")

    def send_upcoming_tasks(self):
        #Sends upcoming tasks#
        print("-------------------------")
        print("Wala pa :P")
        print("-------------------------")
