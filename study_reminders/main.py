from study_reminders import (
    StudentsManager,
    generate_reminder,
    send_reminder,
    log_reminder,
    schedule_reminders
)


def manual_trigger(manager):
    """Manually trigger sending reminders once using scheduler logic."""
    print("\n Manually triggering reminder delivery...\n")
    for student in manager.get_students():
        reminder = generate_reminder(student['name'], student['course'])
        send_reminder(student['email'], reminder)
        log_reminder(student, reminder)
    print("\n Manual trigger complete!\n")

def main():
    print("\n--- Study Reminder Automation ---\n")
    manager = StudentsManager()

    # Display all current students
    print("Current students:")
    manager.list_students()

    # Asks the user for which mode to use
    print("\nChoose an option:")
    print("1. Send reminders immediately (Test Mode)")
    print("2. Schedule reminders at preferred times (Automatic Mode)")
    print("3. Manually trigger scheduled reminders now (Manual Simulation)")

    choice = input("\nEnter 1, 2, or 3: ").strip()

    if choice == "1":
        print("\n Sending test reminders immediately...\n")
        for student in manager.get_students():
            reminder = generate_reminder(student['name'], student['course'])
            send_reminder(student['email'], reminder)
            log_reminder(student, reminder)
        print("\n Test reminders sent successfully!\n")

    elif choice == "2":
        print("\n Starting scheduler (reminders will be sent automatically)...\n")
        scheduler_thread = threading.Thread(
            target=schedule_reminders,
            args=(manager, generate_reminder, send_reminder, log_reminder),
            daemon=True
        )
        scheduler_thread.start()

        try:
            while True:
                pass  # keep the program running
        except KeyboardInterrupt:
            print("\n Scheduler stopped by user.\n")

    elif choice == "3":
        manual_trigger(manager)

    else:
        print("\n Invalid choice. Please restart and enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
