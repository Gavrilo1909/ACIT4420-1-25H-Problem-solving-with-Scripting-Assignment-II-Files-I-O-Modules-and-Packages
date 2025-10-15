# ACIT4420-1-25H-Problem-solving-with-Scripting-Assignment-II-Files-I-O-Modules-and-Packages

This project is developed as part of the ACIT4420-1 25H Problem Solving with Scripting course at OsloMet, Oslo Metropolitan University. It combines scheduling strategies, file handling, and modular programming to show how automation can improve academic time management.

This project's goals are to: 
Maintain student information, such as names, emails, classes, and preferred reminder times.
Make customized study reminders.
Play the role of reminding every student.
Record reminder activities and include timestamps.
Use a scheduling system to automatically send out reminders every day.

# Package Structure
study_reminders/
│
├── init.py
├── logger.py
├── main.py
├── reminder_generator.py
├── reminder_sender.py
├── scheduler.py
├── students_manager.py
├── students.py
│
|── README.md
└── setup.py → Installation configuration

Clone the GitHub repository and navigate into the folder:
git clone https://github.com/Gavrilo1909/ACIT4420-1-25H-Problem-solving-with-Scripting-Assignment-II-Files-I-O-Modules-and-Packages.git
cd ACIT4420-1-25H-Problem-solving-with-Scripting-Assignment-II-Files-I-O-Modules-and-Packages
Install the package locally
Install the package in editable mode so you can run it directly from anywhere:
pip install -e .

After installation, simply run the automation tool using:
studyreminders

You will be met by 3 options:

Option 1 – Immediate (Test Mode): Instantly generates and sends all reminders for testing. Logs results to reminder_log.txt.
Option 2 – Automatic (Scheduler Mode): Starts the continuous scheduler to send reminders automatically at each student’s preferred time.
Option 3 – Manual Simulation: Manually triggers all reminders immediately, simulating the automated schedule for demonstration purposes.

# Logging and Data Management
Operational Logging: Every reminder sent is logged in reminder_log.txt with timestamps for traceability.
Data Storage: Student data is stored in students.json, providing a human-readable and easily modifiable format.
These two systems ensure data persistence and complete transparency of all automated operations.

# Example Program Flow
1. When launched, the program first displays all stored students (name, email, course, and preferred time).
2. The user selects a mode of execution.
3. Depending on the mode, reminders are sent immediately, scheduled to run automatically, or manually triggered.
4. All reminder activities are recorded in the log file.


