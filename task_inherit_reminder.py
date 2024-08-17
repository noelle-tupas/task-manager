from task import Task
from task_reminder import TaskReminder

class TaskWithReminder(Task, TaskReminder):
    def __init__(self, task_name, description, due_date, priority_level, completion_status):
        Task.__init__(self, task_name, description, due_date.split()[0], priority_level, completion_status)
        TaskReminder.__init__(self, due_date)

    def update_and_check_reminder(self):
        '''
        Update task and check if a reminder should be sent.
        '''
        self.check_due_date()