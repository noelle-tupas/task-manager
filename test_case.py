from task import Task
from task_reminder import TaskWithReminder
from task_manager import TaskManager

def main():
    # Create an instance of TaskManager
    task_manager = TaskManager()

    # Add a regular task
    task1 = Task("Complete Assignment", "Finish the assignment for the programming course", "08-20-2024", "high", 50)
    task_manager.add_task(task1)
    
    # Add a task with reminder
    task2 = TaskWithReminder("Doctor Appointment", "Visit the doctor for a check-up", "08-19-2024", "medium", 0, "08-19-2024 09:00 AM")
    task_manager.add_task(task2)

    # Display all tasks
    print("\n--- All Tasks ---")
    for task in task_manager.get_all_tasks():
        print(task.get_task_details())

    # Update completion status of task1
    task1.set_completion_status(100)
    print("\n--- Updated Task 1 Completion Status ---")
    print(task1.get_task_details())

    # Check for reminders
    task_manager.check_reminders()

    # Update the due date of task2 to a past date to trigger reminder
    task2.set_due_date("08-16-2024 09:00 AM")
    task_manager.check_reminders()

if __name__ == "__main__":
    main()
