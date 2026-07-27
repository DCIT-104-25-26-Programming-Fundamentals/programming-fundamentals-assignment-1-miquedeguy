# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(students):
    name = input("Student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return
        
    try:
        student_id_input = input("Student ID: ")
        student_id = int(student_id_input)
    except ValueError:
        print("Error: Student ID must be an integer.")
        return
        
    for s in students:
        if s["id"] == student_id:
            print(f"Error: A student with ID {student_id} already exists.")
            return
            
    try:
        num_scores_input = input("How many scores? ")
        num_scores = int(num_scores_input)
        if num_scores < 0:
            print("Error: Number of scores cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
        
    scores = []
    for i in range(1, num_scores + 1):
        while True:
            try:
                score_input = input(f"Enter score {i}: ")
                score = float(score_input)
                if score == int(score):
                    score = int(score)
                scores.append(score)
                break
            except ValueError:
                print("Error: Invalid score. Please enter a number.")
                
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    if not students:
        print("No student records found.")
        return
        
    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<8}")
    print("-" * 50)
    for s in students:
        scores_str = ", ".join(str(score) for score in s["scores"])
        if s["scores"]:
            avg_score = sum(s["scores"]) / len(s["scores"])
            avg_str = f"{avg_score:.2f}"
        else:
            avg_str = "0.00"
            
        print(f"{s['name']:<15}{s['id']:<12}{scores_str:<15}{avg_str:<8}")
    print("-" * 50)

def calculate_average_for_student(students):
    try:
        search_id_input = input("Enter student ID: ")
        search_id = int(search_id_input)
    except ValueError:
        print("Error: Student ID must be an integer.")
        return
        
    for s in students:
        if s["id"] == search_id:
            if s["scores"]:
                avg_score = sum(s["scores"]) / len(s["scores"])
                print(f"{s['name']}'s average score: {avg_score:.2f}")
            else:
                print(f"{s['name']} has no scores entered.")
            return
            
    print("Error: Student ID not found.")

def main():
    students = []
    while True:
        print("\n================================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
