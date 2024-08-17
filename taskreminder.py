from datetime import datetime

class TaskReminder:
    def __init__(self, due_date):
        # mm-dd-yyyy HH:MM (24-hour format)
        self.__due_date = datetime.strptime(due_date, "%m-%d-%Y %H:%M")
        self.__reminder_sent = False

    def check_due_date(self):
        #Check due date#
        current_time = datetime.now()
        #Sends reminder if not yet sent#
        if current_time >= self.__due_date and not self.__reminder_sent:
            self.send_reminder()
            self.__reminder_sent = True

    def send_reminder(self):
        #Reminder message#
        print(f"Reminder: The task is due on {self.__due_date.strftime('%m-%d-%Y %H:%M')}!")
