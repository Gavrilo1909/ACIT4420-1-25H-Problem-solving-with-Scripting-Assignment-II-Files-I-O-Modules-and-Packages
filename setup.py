from setuptools import setup, find_packages

setup(
    name="studyremindersmodule",  
    version="0.2",
    packages=find_packages(),       
    include_package_data=True,      
    description="A study reminder automation module for ACIT4420 assignment.",
    author="Gavrilo Ilic",
    author_email="gavriloilic@example.com",
    install_requires=[
        "schedule>=1.2.0"  
    ],
    entry_points={
        'console_scripts': [
            'studyreminders=study_reminders.main:main',  # Command to run main()
        ],
    },
)
