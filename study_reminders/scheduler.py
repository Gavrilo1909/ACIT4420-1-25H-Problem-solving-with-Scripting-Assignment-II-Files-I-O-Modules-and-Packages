import schedule
import time
from datetime import datetime

def convert_to_24h(time_str):
    """Convert '08:00 AM' or '07:30 PM' to 24-hour 'HH:MM' format."""
    try:
        return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
    except ValueError:
        return time_str  # already in 24h format

def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """Schedule reminder delivery for each student at their preferred time."""
    for student in students_manager.get_students():
        reminder = reminder_generator(student['name'], student['course'])
        time_24h = convert_to_24h(student['preferred_time'])
        print(f"📅 Scheduling reminder for {student['name']} at {time_24h}")
        schedule.every().day.at(time_24h).do(
            lambda s=student, r=reminder: (reminder_sender(s['email'], r), logger(s, r))
        )

    while True:
        schedule.run_pending()
        time.sleep(60)

