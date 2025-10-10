from setuptools import setup, find_packages

setup(
    name="studyremindersmodule",  # Your package name (use underscores, not spaces)
    version="0.2",
    packages=find_packages(),       # Automatically find all subpackages
    include_package_data=True,      # Include non-Python files if needed
    description="A study reminder automation module for ACIT4420 assignment.",
    author="Gavrilo Ilic",
    author_email="gavriloilic@example.com",
    install_requires=[
        "schedule>=1.2.0"  # The only required external dependency
    ],
    entry_points={
        'console_scripts': [
            'studyreminders=study_reminders.main:main',  # Command to run main()
        ],
    },
)
