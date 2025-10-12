"""
CP1404/CP5632 - Practical 4
Mikhail Bovt
12/10/2025
Converting Data Strings to Lists
"""
import os

FILENAME = os.path.join(os.path.dirname(__file__), "subject_data.txt")


def main():
    """Load subject data and display each subject details."""
    subjects = load_subject_data(FILENAME)
    display_subject_details(subjects)


def load_subject_data(filename):
    """Read data from file formatted and return a list of lists."""
    subject_records = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(",")
            parts[2] = int(parts[2]) 
            subject_records.append(parts)
    return subject_records


def display_subject_details(subjects):
    """Display formatted subject details."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")


main()
