# main.py

from study_reminders.students_manager import StudentsManager
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder
from study_reminders.logger import log_reminder
from study_reminders.scheduler import schedule_reminders
import threading

def send_all_reminders_once(students_manager):
    """Send reminders to all students immediately (for testing)."""
    for student in students_manager.get_students():
        reminder = generate_reminder(student['name'], student['course'])
        send_reminder(student['email'], reminder)
        log_reminder(student, reminder)

def main():
    # Initialize StudentsManager
    sm = StudentsManager()

    # List all students
    print("Current students:")
    sm.list_students()
    print("\nSending test reminders...\n")

    # Send all reminders once for testing
    send_all_reminders_once(sm)

    # Schedule daily reminders (non-blocking using threading)
    print("\nStarting scheduler (reminders will be sent at preferred times)...")
    scheduler_thread = threading.Thread(
        target=schedule_reminders, 
        args=(sm, generate_reminder, send_reminder, log_reminder),
        daemon=True
    )
    scheduler_thread.start()

    # Keep the main script running to allow the scheduler to work
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")

if __name__ == "__main__":
    main()
